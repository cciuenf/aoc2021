{
  description = "Soluções do Advent of Code 2021";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages."${system}";

        elixir_1_12 = pkgs.beam.packages.erlangR24.elixir.override {
          version = "1.12.2";
          minimumOTPVersion = "24";
          sha256 = "1f8b63x2klhdz1fq1dgbrqs7x6rq309abzq48gicmd0vprfhc641";
        };
      in {
        devShell = pkgs.mkShell {
          name = "aoc2021";
          buildInputs = with pkgs; [
            # base pkgs
            gnumake
            readline
            openssl
            zlib
            libxml2
            curl
            libiconv
            glibcLocales

            # langs
            ## C
            gcc
            # python
            python3
            # js
            nodejs
            ## elixir
            elixir_1_12
            ## haskell
            stack ghc haskellPackages.fourmolu
          ] ++ pkgs.lib.optional stdenv.isLinux [
            inotify-tools
            gtk-engine-murrine
          ] ++ pkgs.lib.optionals stdenv.isDarwin (with darwin.apple_sdk.frameworks; [
            CoreFoundation
            CoreServices
          ]);
        };
      });
}
