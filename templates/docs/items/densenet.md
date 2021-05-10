<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<title>Image Prediction using PyTorch</title>
	<meta name="theme-color" content="#f2f4f6">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@9/dist/sweetalert2.min.css" id="theme-styles">
	<style>
      #evanyou {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: -1;
      }
    </style>
	<style type="text/css">
		html {
		    font-family: sans-serif;
		    line-height: 1.15;
		    -webkit-text-size-adjust: 100%;
		    -webkit-tap-highlight-color: transparent;
		}
		html, body {
		  height: 100%;
		}

		body {
		  display: -ms-flexbox;
		  display: flex;
		  -ms-flex-align: center;
		  align-items: center;
		  padding-top: 40px;
		  padding-bottom: 40px;
		  background-color: #f5f5f5;
		}

		body {
		    margin: 0;
		    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";
		    font-size: 1rem;
		    font-weight: 400;
		    line-height: 1.5;
		    color: #212529;
		    text-align: left;
		    background-color: #fff;
		}

		*, ::after, ::before {
		    box-sizing: border-box;
		}

		.h1, .h2, .h3, .h4, .h5, .h6, h1, h2, h3, h4, h5, h6 {
		    margin-bottom: .5rem;
		    font-family: inherit;
		    font-weight: 500;
		    line-height: 1.2;
		    color: inherit;
		}
		.h1, h1 {
		    font-size: 2.5rem;
		}
		h1, h2, h3, h4, h5, h6 {
		    margin-top: 0;
		    margin-bottom: .5rem;
		}
		.h3, h3 {
		    font-size: 1.75rem;
		}

		.form-signin {
		  width: 100%;
		  max-width: 330px;
		  padding: 15px;
		  margin: auto;
		}

		.form-signin .form-control {
		  position: relative;
		  box-sizing: border-box;
		  height: auto;
		  padding: 10px;
		  font-size: 16px;
		}

		.mb-3, .my-3 {
		    margin-bottom: 1rem!important;
		}

		.mb-4, .my-4 {
		    margin-bottom: 1.5rem!important;
		}

		.mt-5, .my-5 {
		    margin-top: 3rem!important;
		}

		p {
		    display: block;
		    margin-block-start: 1em;
		    margin-block-end: 1em;
		    margin-inline-start: 0px;
		    margin-inline-end: 0px;
		}

		img {
		    vertical-align: middle;
		    border-style: none;
		}

		img[Attributes Style] {
		    width: 72px;
		}
		.text-center {
    		text-align: center!important;
		}

		.text-muted {
		    color: #6c757d!important;
		}

		.font-weight-normal {
		    font-weight: 400!important;
		}

		.form-control-file, .form-control-range {
		    display: block;
		    width: 100%;
		}

		.btn:not(:disabled):not(.disabled) {
		   cursor: pointer;
		}

		.btn-block {
		    width: 100%;
		}
		
		.btn {
		    display: inline-block;
		    font-weight: 400;
		    text-align: center;
		    vertical-align: middle;
		    user-select: none;
		    border: 1px solid transparent;
		    padding: .375rem .75rem;
		    font-size: 1rem;
		    line-height: 1.5;
		    border-radius: .25rem;
		    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
		}

		.upload-button {
		    border: 1px solid #ccc;
		    border-radius: 33px;
		    padding: 10px 30px;
		    background-color: rgba(0, 0, 0, 0);
		    display: inline-block;
		    margin-right: 10px;
		    color: #333;
		}
		
		.btn-primary {
		    color: #fff;
		    background-color: #007bff;
		    border-color: #007bff;
		}
		button {
		    appearance: button;
		    -webkit-writing-mode: horizontal-tb !important;
		    text-rendering: auto;
		    letter-spacing: normal;
		    word-spacing: normal;
		    text-transform: none;
		    text-indent: 0px;
		    text-shadow: none;
		    align-items: flex-start;
		    box-sizing: border-box;
		    margin: 0em;
		    font: 400 13.3333px Arial;
		    border-image: initial;
		    border-radius: 2px;
		}
	</style>
	<script src="https://cdn.jsdelivr.net/npm/sweetalert2@9/dist/sweetalert2.min.js"></script>
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
	
</head>
<body class="text-center">
   	<canvas id="evanyou"></canvas>
    <script src="evanyou.js"></script>

	<form class="form-signin" method="post" enctype="multipart/form-data">
        <img class="mb-4" src="https://pytorch-imagenet.herokuapp.com/static/pytorch.png" alt="" width="72">
        <h1 class="h3 mb-3 font-weight-normal">Upload any image</h1>
        <input type="file" name="file" class="form-control-file upload-button" id="inputfile">
        <br><br>
        <button class="btn btn-lg btn-block upload-button" type="submit">Upload</button>
        <p class="mt-5 mb-3 text-muted">Built using Pytorch, Flask and Love</p>
	</form>

	<a href="https://github.com/jamesyangget/densenet-pytorch-fastapi" class="github-corner" aria-label="View source on GitHub">
		<svg width="80" height="80" viewBox="0 0 250 250" style="fill:#64ceaa; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true">
			<path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
			<path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
			<path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path>
		</svg>
	</a>

    <script type="text/javascript">
      $('#inputfile').bind('change', function() {
      	  //判断图片大小
          let fileSize = this.files[0].size/1024/1024; // this gives in MB
          if (fileSize > 1) {
            $("#inputfile").val(null);
			Swal.fire({
			  title: 'Oops...',
			  icon: 'error',
			  text: 'file is too big. images more than 1MB are not allowed!',
			  timer: 3000,
			  showConfirmButton: false
			})
            return
          }

          //判断图片格式
          let ext = $('#inputfile').val().split('.').pop().toLowerCase();
          if($.inArray(ext, ['png','jpg','jpeg']) == -1) {
            $("#inputfile").val(null);
            Swal.fire({
			  title: 'Oops...',
			  icon: 'error',
			  text: 'only png/jpg/jpeg files are allowed!',
			  timer: 3000,
			  showConfirmButton: false
			})
          }
      });
    </script>

</body>
</html>
