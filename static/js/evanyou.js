(function () {
    let c = document.getElementById('evanyou'),
        x = c.getContext('2d'),
        pr = window.devicePixelRatio || 1,
        w = window.innerWidth,
        h = window.innerHeight,
        f = 90,
        q,
        m = Math,
        r = 0,
        u = m.PI * 2,
        v = m.cos,
        z = m.random;
    c.width = w * pr;
    c.height = h * pr;
    x.scale(pr, pr);
    x.globalAlpha = 0.6;

    function ey() {
        x.clearRect(0, 0, w, h);
        q = [{x: 0, y: h * .7 + f}, {x: 0, y: h * .7 - f}];
        while (q[1].x < w + f) d(q[0], q[1]);
    }

    function d(i, j) {
        x.beginPath();
        x.moveTo(i.x, i.y);
        x.lineTo(j.x, j.y);
        let k = j.x + (z() * 2 - 0.25) * f, n = y(j.y);
        x.lineTo(k, n);
        x.closePath();
        r -= u / -50;
        x.fillStyle = '#' + (v(r) * 127 + 128 << 16 | v(r + u / 3) * 127 + 128 << 8 | v(r + u / 3 * 2) * 127 + 128).toString(16);
        x.fill();
        q[0] = q[1];
        q[1] = {x: k, y: n};
    }

    function y(p) {
        let t = p + (z() * 2 - 1.1) * f;
        return (t > h || t < 0) ? y(p) : t;
    }

    function evanyou() {
        document.onclick = ey;
        document.ontouchstart = ey;
        setInterval(function () {
            evanyou();
        }, 2000);//设置定时2秒运行
    }

    function install(hook) {
        if (!$docsify.evanyou) {
            console.error('[Docsify] evanyou is required.');
            return;
        }

        var dom = Docsify.dom;

        hook.mounted(function (_) {
            var canvas = dom.create('canvas');
            canvas.id = 'evanyou';
            var main = dom.getNode('#main');
            // div.style = "width: " + (main.clientWidth) + "px; margin: 0 auto 20px;";
            dom.appendTo(main, div);
        });

        hook.beforeEach(evanyou);
    }

    $docsify.plugins = [].concat(install, $docsify.plugins);

}());