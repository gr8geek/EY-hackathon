document.addEventListener('DOMContentLoaded', function() {
    console.log("Hello World")
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {
        opacity:0.5,
    });
  });
  /**
   * 
   * Sending Single resume at a time to the server
   * 
   */
  /*
  var submitButton = document.getElementById("")
  submitButton.onclick = function() {
    var file = document.getElementById('file').files[0];
    var formData = new FormData();
    formData.append('file', file);
    formData.append('JD', document.getElementById('JD').value);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/file-upload', true);
    console.log("Hie")
    xhr.onload = function() {
      if (xhr.status === 201) {
      }
    };
    xhr.send(formData);
  };
  */