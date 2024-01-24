<div class="mkap-window">
    <div class="mkap-menu">
        <div class="mkap-button mkap-button-close"></div>
        <div class="mkap-button mkap-button-minimize"></div>
        <div class="mkap-button mkap-button-zoom"></div>
        <div class="mkap-button-title">Terminal</div>
    </div>
    <div class="mkap-player" id="asciinema-player-0"></div>
</div>
<script>
    window.addEventListener("load", function(event) {
        AsciinemaPlayer.create("/example-group/project-name/assets/asciinema/test.cast", document.getElementById("asciinema-player-0"), {
            cols: 120,
            rows: 24,
            autoPlay: true,
            preload: false,
            loop: false,
            startAt: "0:00",
            speed: 1.0,
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