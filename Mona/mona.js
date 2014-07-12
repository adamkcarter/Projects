/* =======================================================
 *  ---- HTML5 CANVAS fractal painting ----
 * script: Gerard Ferrandez - 6 April 2013
 * Released under the MIT license
 * http://www.dhteumeuleu.com/LICENSE.html
 * ======================================================= */
 
"use strict";

(function () {
	var scr, ctx, pointer, imgdata, root = {}, W, H;
	// ==== init script ====
	var init = function () {
		// ---- screen ----
		scr = new ge1doot.Screen({
			container: "screen",
			resize: function () {
				// ---- resize ----
				W = ic.width  = scr.width;
				H = ic.height = scr.height;
				// ---- image data ----
				var ict = ic.getContext('2d');
				ict.drawImage(img, 0, 0, W, H);
				imgdata = ict.getImageData(0, 0, W, H).data;
				// ---- split root ----
				root = {};
				div (root, 0, 0, W, H);
			}
		});
		ctx = scr.ctx;
		// ---- pointer events ----
		pointer = new ge1doot.Pointer({
			move: function () {
				paint(root, pointer.X, pointer.Y);
			},
			tap: function () {
				paint(root, pointer.X, pointer.Y);
			}
		});
		// ---- original image ----
		var img = document.getElementById("source");
		var ic = document.createElement('canvas');
		scr.resize();
	}
	// ==== divide ====
	var div = function (o, x, y, w, h) {
		// ---- clear background ----
		if (w > 12) {
			ctx.fillStyle = "#000";
			ctx.fillRect(x, y, w, h);
		}
		// ---- split area ----
		w = w * 0.5;
		h = h * 0.5;
		o.children = [];
		o.children[0] = new Pix(x, y, w, h);
		o.children[1] = new Pix(x + w, y, w, h);
		o.children[2] = new Pix(x, y + h, w, h);
		o.children[3] = new Pix(x + w, y + h, w, h);
	}
	// ==== pixel constructor ====
	var Pix = function (x, y, w, h) {
		// ---- coordinates ----
		this.x = x;
		this.y = y;
		this.w = w;
		this.h = h;
		// ---- read color from image data ----
		var cx = Math.round(x + w * 0.5);
		var cy = Math.round(y + h * 0.5);
		var r = imgdata[((W * cy) + cx) * 4];
		var g = imgdata[((W * cy) + cx) * 4 + 1];
		var b = imgdata[((W * cy) + cx) * 4 + 2];
		// ---- set painting color ----
		ctx.fillStyle = 'rgb(' + r + ',' + g + ',' + b + ')';
		if (Math.max(w, h) > 6) {
			// ---- oval ----
			ctx.save();
			ctx.beginPath();
			if (w > h) {
				// ---- paysage ----
				ctx.scale(1, h / w);
				ctx.arc(cx, cy * w / h, Math.max(w * 0.5, h * 0.5), 0, 2 * Math.PI, false);
			} else {
				// ---- portrait ----
				ctx.scale(w / h, 1);
				ctx.arc(cx * h / w, cy, Math.max(w * 0.5, h * 0.5), 0, 2 * Math.PI, false);
			}
			ctx.fill();
			ctx.restore();
		} else {
			// ---- pixel ----
			ctx.fillRect(x, y, w, h);
		}
	}
	// ==== recursive paint ====
	var paint = function (o, x, y) {
		for (var i = 0; i < 4; i++) {
			var oc = o.children[i];
			// ---- pointer inside ----
			if (
				x >= oc.x && x <= oc.x + oc.w &&
				y >= oc.y && y <= oc.y + oc.h
			) {
				// ---- next node ----
				if (oc.children) paint(oc, x, y);
				// ---- divide leaf ----
				else if (oc.w > 1 || oc.h > 1) {
					div (oc, oc.x, oc.y, oc.w, oc.h);
				}
				break;
			}
		}
	}
	return {
		// ---- onload event ----
		load : function () {
			window.addEventListener('load', function () {
				init();
			}, false);
		}
	}
})().load();