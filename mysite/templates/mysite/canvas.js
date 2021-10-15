    var ocrInfo = {
      imgUrl : '{% get_static_prefix %}upload/{{page.filename}}_{{page.page_num}}.box.jpg',
      textLoc : tesseract_ocr_extract('{% get_static_prefix %}upload/{{page.filename}}_{{page.page_num}}.box.jpg')
    }

   // set Canvas
   setCanvas(ocrInfo);

    /**
    * Canvas 설정
    */
    var setCanvas = function(ocrInfo){
    var canvas = document.getElementById('canvas');
    	if (canvas.getContext) {

            var ctx = canvas.getContext('2d');
            var imageObj = new Image();
	        imageObj.onload = function () {
	        	canvas.width=360;
	        	canvas.height=203;
	        	ctx.drawImage(imageObj, 0, 0, 360, 203);

	        	// multi boxing 처리
	        	$.each(ocrInfo.textLoc, function(key, item){
	 	        	ctx.strokeStyle = item.color;
	 	        	ctx.lineWidth = 3;
	 	        	ctx.strokeRect(item.x, item.y, item.w, item.h);

	 	        	// Text 처리
	 	        	ctx.textBaseline = 'top';
	 	        	ctx.font="13px Verdana";
	 	        	ctx.fillStyle = "red";
	 	        	ctx.fillText(item.text, item.x, item.y + item.h + 5);
	 	        	ctx.fill();
	        	});
	        };
	        imageObj.src = ocrInfo.imgUrl;
		}
	};