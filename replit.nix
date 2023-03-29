{ pkgs }: {
	deps = [
		pkgs.mariadb
		pkgs.python39
		pkgs.python39Packages.pip
	];
}