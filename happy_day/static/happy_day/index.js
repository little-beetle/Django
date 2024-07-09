document.addEventListener('DOMContentLoaded', function () {
    var elm = document.querySelector('#main-header');
    var lavalampElm = document.querySelector('.lavalamp');

    if (elm) {
        var ms = new MenuSpy(elm, {
            callback: positionLavalamp
        });

        var positionLavalamp = function(activeElm) {
            if (lavalampElm) {
                lavalampElm.style.width = activeElm.elm.offsetWidth + 'px';
                lavalampElm.style.left = activeElm.elm.offsetLeft + 'px';
            }
        };

        positionLavalamp({ elm: elm.querySelector('li.active') });
    }
});
