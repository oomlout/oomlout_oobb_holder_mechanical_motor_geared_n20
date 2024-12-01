$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-13.2500000000, 2.0000000000, 0]) {
				cylinder(h = 30, r = 5);
			}
			translate(v = [13.2500000000, 2.0000000000, 0]) {
				cylinder(h = 30, r = 5);
			}
			translate(v = [-13.2500000000, -2.0000000000, 0]) {
				cylinder(h = 30, r = 5);
			}
			translate(v = [13.2500000000, -2.0000000000, 0]) {
				cylinder(h = 30, r = 5);
			}
		}
	}
	union() {
		translate(v = [11.2500000000, 0, 15.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 50, r = 3.6000000000);
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.8000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-11.2500000000, 0, 15.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.5000000000);
						}
						#translate(v = [0, 0, -1.9000000000]) {
							cylinder(h = 1.9000000000, r1 = 1.8000000000, r2 = 3.6000000000);
						}
						#cylinder(h = 50, r = 3.6000000000);
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.8000000000);
						}
						#translate(v = [0, 0, -30.0000000000]) {
							cylinder(h = 30, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [4.5000000000, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 0.8500000000);
						}
						translate(v = [0, 0, -1.2000000000]) {
							cylinder(h = 1.2000000000, r1 = 1.1000000000, r2 = 1.7500000000);
						}
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 1.1000000000);
						}
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 0.8500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-4.5000000000, 0, 30]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 0.8500000000);
						}
						translate(v = [0, 0, -1.2000000000]) {
							cylinder(h = 1.2000000000, r1 = 1.1000000000, r2 = 1.7500000000);
						}
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 1.1000000000);
						}
						translate(v = [0, 0, -4.0000000000]) {
							cylinder(h = 4, r = 0.8500000000);
						}
					}
					union();
				}
			}
		}
		#translate(v = [-7.0000000000, -5.5000000000, 0]) {
			cube(size = [14, 11, 27.5000000000]);
		}
		cylinder(h = 30, r = 2.2500000000);
		translate(v = [-1.5000000000, -18.7500000000, 0]) {
			cube(size = [3, 37.5000000000, 3]);
		}
	}
}