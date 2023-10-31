<div style="padding-top:15px; background-color: #acacac; border-radius: 3%">
    <span style="display: flex; margin-bottom: 10px">
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: green; border-radius:50%"></div>
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: orange; border-radius:50%"></div>
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: red; border-radius:50%"></div>
    </span>
    <div id="clone-and-test"></div>
</div>
<script>
    window.onload = function(){
        AsciinemaPlayer.create('/example-group/project-name/test.cast', document.getElementById('clone-and-test'), {
            loop: true,
            cols: 120,
            rows: 25,
            autoPlay: true,
            terminalFontSize: "big"
        });
    }
</script>