$(document).ready(function () {
    var viewer = OpenSeadragon({
        id: "openseadragon",
        prefixUrl: "/static/transcribe/osd/",
        tileSources: "/static/transcribe/dzi/" + fileid + ".dzi",
    });
});
