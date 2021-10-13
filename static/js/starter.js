var loader = document.getElementById('loader');

window.addEventListener('load', function(){
    this.setInterval(frame, 500);
    function frame(){
        loader.style.display = 'none';
    }
})