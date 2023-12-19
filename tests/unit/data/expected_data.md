<div style="padding-top:15px; background-color: #acacac; border-radius: 3%">
    <span style="display: flex; margin-bottom: 10px">
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: green; border-radius:50%"></div>
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: orange; border-radius:50%"></div>
        <div style="width: 15px; height: 15px; margin-left:5px; background-color: red; border-radius:50%"></div>
    </span>
    <div id="asciinema-player-0"></div>
</div>
<script>
    window.addEventListener("load", function(event) {
        AsciinemaPlayer.create("/example-group/project-name/assets/asciinema/test.cast", document.getElementById("asciinema-player-0"), {
            cols: 120,
            rows: 24,
            autoPlay: true,
            preload: false,
            loop: false,
            startAt: 0,
            speed: 1,
            theme: "asciinema",
            fit: "width",
            controls: "auto",
            pauseOnMarkers: false,
            terminalFontSize: "small",
            terminalFontFamily: "Consolas",
            terminalLineHeight: 1.33333333,
        });
    });
</script>