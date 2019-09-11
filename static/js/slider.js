"use strict";
var Slider = function(a) {
    this.i = 0;
    this.objid = a.objid || null;
    this.preclassname = a.preclassname || ".btn-prev";
    this.nextclassname = a.nextclassname || ".btn-next";
    this.listname = a.listname || ".grid-list";
    this.listitem = a.listitem || "li";
    this.shownum = a.shownum || 5.5;
    this.type = a.type || 1;
    this.autoplay = a.autoplay || false;
    this.offset = a.offset || 0
};
Slider.prototype = {
    init: function() {
        var b = this;
        var a = b.set();
        if (b.autoplay) {
            b.auto(a)
        } else {
            b.next(a);
            b.pre(a)
        }
    },
    auto: function(e) {
        var d = this,
            c = null;
        $(d.listname).find(d.listitem).eq(0).clone().appendTo(d.listname);
        e.len += 1;
        var b = (e.itemHeight) * (e.len - 1),
            a = function() {
                d.i++;
                if (Math.abs(parseInt(e.$grid.css("margin-top"))) == b) {
                    e.$grid.css("margin-top", 0);
                    d.i = 1
                }
                e.$grid.animate({
                    "margin-top": "-" + (d.i * e.itemHeight * d.shownum) + "px"
                }, 500)
            };
        if (d.autoplay) {
            c = setInterval(a, 2000);
            e.$grid.hover(function() {
                clearInterval(c)
            }, function() {
                c = setInterval(a, 2000)
            })
        }
    },
    set: function() {
        var e = this,
            h = $(e.objid + " " + e.listitem),
            j = $(e.objid + " " + e.listname),
            i = $(e.objid + " " + e.preclassname),
            b = $(e.objid + " " + e.nextclassname),
            f = h.length,
            g = h.outerWidth(),
            a = h.outerHeight(),
            d = Math.ceil(f / e.shownum),
            c = 0;
        switch (e.type) {
            default:
            case 1:
                j.css("width", (g + 1) * f + "px");
                break;
            case 2:
                j.css("height", (a) * f + "px");
                break;
            case 3:
                g = g + 20;
                j.css("width", (g) * f + "px");
                break;
            case 4:
                g = g + 50;
                j.css("width", (g) * f + "px");
                break;
            case 5:
                j.css("width", (g + 1) * f + "px");
                if (f <= e.shownum) {
                    b.addClass("disabled")
                } else {
                    b.removeClass("disabled")
                }
                break
        }
        return {
            $item: h,
            $grid: j,
            $pre: i,
            $next: b,
            len: f,
            itemWidth: g,
            itemHeight: a,
            num: d,
            offset: c
        }
    },
    pre: function(b) {
        var a = this;
        b.$pre.bind("click", function() {
            if ($(this).hasClass("disabled")) {
                return
            }
            a.i--;
            a.offset -= a.shownum;
            if (a.i - 1 < 0) {
                b.$pre.addClass("disabled")
            }
            b.$next.removeClass("disabled");
            switch (a.type) {
                default:
                case 1:
                    b.$grid.animate({
                        "margin-left": a.i == 0 ? 0 : parseInt(b.$grid.css("margin-left")) + (b.itemWidth * a.shownum) + "px"
                    }, 500);
                    break;
                case 2:
                    b.$grid.animate({
                        "margin-top": a.i == 0 ? 0 : parseInt(b.$grid.css("margin-top")) + (b.itemHeight * a.shownum) + "px"
                    }, 500);
                    break;
                case 3:
                case 4:
                    if (a.offset < 0) {
                        a.offset = 0;
                        b.$pre.addClass("disabled")
                    }
                    b.$grid.animate({
                        "margin-left": "-" + (a.offset * b.itemWidth) + "px"
                    }, 500);
                    break;
                case 5:
                    b.$grid.animate({
                        "margin-left": a.i == 0 ? 0 : parseInt(b.$grid.css("margin-left")) + (b.itemWidth * a.shownum) + "px"
                    }, 500);
                    break
            }
        })
    },
    next: function(b) {
        var a = this;
        switch (a.type) {
            case 3:
            case 4:
                if (a.offset + 1 >= b.num) {
                    b.$next.addClass("disabled")
                }
                break
        }
        b.$next.bind("click", function() {
            if ($(this).hasClass("disabled")) {
                return
            }
            a.i++;
            a.offset += a.shownum;
            b.$pre.removeClass("disabled");
            switch (a.type) {
                default:
                case 1:
                    if (a.shownum > 1) {
                        if (a.i + 1 == b.num) {
                            var d = parseInt(b.$grid.css("margin-left"));
                            var c = (b.len - ((a.i) * parseInt(a.shownum)) - 1 / 2) * b.itemWidth;
                            b.$grid.animate({
                                "margin-left": d - c + "px"
                            }, 500)
                        } else {
                            b.$grid.animate({
                                "margin-left": "-" + (a.i * b.itemWidth * parseInt(a.shownum)) + "px"
                            }, 500)
                        }
                    } else {
                        b.$grid.animate({
                            "margin-left": "-" + (a.i * b.itemWidth * a.shownum) + "px"
                        }, 500)
                    }
                    if (a.i + 1 == b.num) {
                        b.$next.addClass("disabled")
                    }
                    break;
                case 2:
                    b.$grid.animate({
                        "margin-top": "-" + (a.i * b.itemHeight * a.shownum) + "px"
                    }, 500);
                    if (a.i + 1 == b.num) {
                        b.$next.addClass("disabled")
                    }
                    break;
                case 3:
                case 4:
                    if (a.offset + a.shownum > b.len) {
                        a.offset = b.len - a.shownum;
                        b.$grid.animate({
                            "margin-left": "-" + (a.offset * b.itemWidth) + "px"
                        }, 500);
                        b.$next.addClass("disabled")
                    } else {
                        b.$grid.animate({
                            "margin-left": "-" + (a.offset * b.itemWidth) + "px"
                        }, 500)
                    }
                    break;
                case 5:
                    if (a.shownum > 1) {
                        if (a.i + 1 == b.num) {
                            var d = parseInt(b.$grid.css("margin-left"));
                            var c = (b.len - ((a.i) * parseInt(a.shownum))) * b.itemWidth;
                            b.$grid.animate({
                                "margin-left": d - c + "px"
                            }, 500)
                        } else {
                            b.$grid.animate({
                                "margin-left": "-" + (a.i * b.itemWidth * parseInt(a.shownum)) + "px"
                            }, 500)
                        }
                    } else {
                        b.$grid.animate({
                            "margin-left": "-" + (a.i * b.itemWidth * a.shownum) + "px"
                        }, 500)
                    }
                    if (a.i + 1 == b.num) {
                        b.$next.addClass("disabled")
                    }
                    break
            }
        })
    }
};
