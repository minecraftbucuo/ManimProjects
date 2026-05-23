{
  description = "Manim Animation Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nixgl.url = "github:nix-community/nixGL"; # 👈 新增：引入 nixGL 源
  };

  outputs = { self, nixpkgs, nixgl }: # 👈 新增：接收 nixgl
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      # 1. 声明系统级依赖
      packages = with pkgs; [
        python312
        python312Packages.pip
        python312Packages.venvShellHook # 这个钩子会自动帮你管理虚拟环境
        python312Packages.setuptools

        # Manim 底层媒体与渲染依赖
        ffmpeg
        cairo
        pango
        pkg-config

        # LaTeX 环境，用于渲染数学公式
        # 注意：scheme-full 体积较大 (约 5GB)，但能保证你用任何 LaTeX 宏包都不会报错。
        # 如果你想省空间，可以换成 texlive.combined.scheme-medium
        texlive.combined.scheme-full
        
        # 补丁：引入 C++ 标准库和 zlib，解决 NumPy 等预编译包找不到动态库的问题
        stdenv.cc.cc.lib
        zlib

        # 👈 新增：注入无后缀的 nixGL 环境包 (nixGLDefault 提供 nixGL 命令)
        nixgl.packages.${system}.nixGLDefault
      ];

      # 2. 告诉 Nix 虚拟环境建在哪里
      venvDir = "./.venv";

      # 3. 首次创建虚拟环境时自动执行的脚本
      postVenvCreation = ''
        unset SOURCE_DATE_EPOCH
        echo "正在根据 requirements.txt 安装依赖..."
        pip install -r requirements.txt
      '';

      # 4. 每次进入这个 nix develop 环境时执行的脚本
      postShellHook = ''
        unset SOURCE_DATE_EPOCH
        # 这一步非常关键：确保通过 pip 下载的 manimpango 和 numpy 能够找到系统的动态库
        export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath (with pkgs; [ cairo pango glib stdenv.cc.cc.lib zlib ])}:$LD_LIBRARY_PATH"
        
        # 👈 新增：自动设置别名，直接使用无后缀的 nixGL 启动 manimgl
        alias manimgl="nixGL manimgl"
      '';
    };
  };
}