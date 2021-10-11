class PostData{
    constructor(type,url,data,session){
        this.type = type;
        this.url = url;
        this.data = data;
        this.session = session;
    }
     Start(){
        if(this.type == 'resz'){
            submitButton.onclick = function() {
                var file = document.getElementById(this.data).files[0];
                var formData = new FormData();
                formData.append('file', file);
                formData.append('session',this.session)

                formData.append('dataID',str );
                localStorage.setItem(str,'')
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/file-upload-zip', true);
                console.log("Hie")
                xhr.onload = function() {
                  if (xhr.status === 201) {
                    var response = JSON.parse(xhr.responseText);
                    console.log(xhr.responseText)
                    console.log(response['Skills'])
                    console.log(response+"resp");
                    }
                };
                xhr.send(formData);
              };
              
        }

        if(this.type == 'res'){
            submitButton.onclick = function() {
                var file = document.getElementById(this.data).files[0];
                var formData = new FormData();
                formData.append('file', file);
                formData.append('session',this.session)


                formData.append('dataID',str );
                localStorage.setItem(str,'')
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/file-upload', true);
                console.log("Hie")
                xhr.onload = function() {
                  if (xhr.status === 201) {
                    var response = JSON.parse(xhr.responseText);
                    console.log(xhr.responseText)
                    console.log(response['Skills'])
                    console.log(response+"resp");
                    }
                };
                xhr.send(formData);
              };

        }
        if(this.type == 'JDf'){
            submitButton.onclick = function() {
                var file = document.getElementById(this.data).files[0];
                var formData = new FormData();
                formData.append('file', file);
                formData.append('session',this.session)

                var str = '';
                formData.append('dataID',str );
                localStorage.setItem(str,'')
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/file-upload', true);
                console.log("Hie")
                xhr.onload = function() {
                  if (xhr.status === 201) {
                    var response = JSON.parse(xhr.responseText);
                    console.log(xhr.responseText)
                    console.log(response['Skills'])
                    console.log(response+"resp");
                    }
                };
                xhr.send(formData);
              };
        }
        if(this.type == 'JD'){
            submitButton.onclick = function() {
                var file = document.getElementById(this.data).files[0];
                var formData = new FormData();
                formData.append('text', file);
                formData.append('session',this.session)

                var str = '';
                for(var i = 0;i<50;i++){
                    str += String.fromCharCode(Math.random()*26+97)
                }

                formData.append('dataID',str );
                localStorage.setItem(str,'')
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/file-upload', true);
                console.log("Hie")
                xhr.onload = function() {
                  if (xhr.status === 201) {
                    var response = JSON.parse(xhr.responseText);
                    console.log(xhr.responseText)
                    console.log(response['Skills'])
                    console.log(response+"resp");
                    }
                };
                xhr.send(formData);
              };
        }
    }
}