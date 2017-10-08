function processFaces(imgId, canvasId, facesId, imageData) {
    var img = document.getElementById(imgId);
    var cnvs = document.getElementById(canvasId);

    // Set the canvas position
    cnvs.style.position = "absolute";
    cnvs.height = img.height;
    cnvs.width = img.width;
    cnvs.style.left = 0; //img.offsetLeft + "px";
    cnvs.style.top = 0; // img.offsetTop + "px";

    var ulFaces = document.getElementById(facesId);
    var faceLike = ["joyLikelihood", "sorrowLikelihood", "angerLikelihood",
                    "surpriseLikelihood", "underExposedLikelihood", "blurredLikelihood",
                    "headwearLikelihood"];

    // Let's draw faces boxes (if found)
    var ctx = cnvs.getContext("2d");
    for (var i in imageData.faceAnnotations) {
        vertx = imageData.faceAnnotations[i].fdBoundingPoly.vertices
        ctx.beginPath();
        console.log(vertx)
        console.log([img.height, img.width])
        ctx.rect(vertx[0].x, vertx[0].y, vertx[2].x-vertx[3].x, vertx[2].y-vertx[1].y)
        ctx.lineWidth = 3;
        ctx.strokeStyle = '#00ff00';
        ctx.stroke();
        // Write the Face name
        ctx.font="30px Verdana";
        ctx.fillStyle="#fff";
        ctx.fillText("Face "+i,vertx[0].x+10, vertx[0].y+30);

        // Add some context information
        liFace = document.createElement('li');
        liFace.innerHTML = 'Face ' + i;
        ulFaces.appendChild(liFace);
        ul = document.createElement('ul');
        liFace.appendChild(ul);
        li = document.createElement('li');
        ul.appendChild(li);
        li.innerHTML = 'detection score: ' + imageData.faceAnnotations[i].detectionConfidence.toFixed(4);
        // Iterate over face like
        for (var j in faceLike) {
            fl = faceLike[j];
            li = document.createElement('li');
            li.innerHTML = fl + ": " + imageData.faceAnnotations[i][fl];
            ul.appendChild(li);
        }
    }
}

function getInformation(imageLabels, imageData) {
    // populate labels (in order of scores)
    var labels = imageData.labelAnnotations.map(function(item){
        return {
            name: item.description,
            score: item.score
        }
    })
    labels = labels.sort(function(a, b) {
        return a.score < b.score ? 1 : -1;
    });
    var ulImageLabels = document.getElementById(imageLabels);
    for (item in labels) {
        var li = document.createElement('li');
        ulImageLabels.appendChild(li);
        li.innerHTML = labels[item].name + " (" + labels[item].score.toFixed(2) + ")";
    }

    //
}