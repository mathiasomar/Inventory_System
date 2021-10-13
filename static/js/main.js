var alert = document.getElementById('alert');


window.addEventListener('load', function(){
    this.setInterval(frame, 3000);
    function frame(){
        alert.style.display = 'none';
    }
})