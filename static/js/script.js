var skillsvec = null;
var skillsname = null;
var skillsid = []
class Data {
  constructor(name,score){
    this.name = name;
    this.score = score;
  }
}
document.addEventListener('DOMContentLoaded', function() {
    console.log("Hello World")
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {
        opacity:0.5,
    });

  })
      async function uploadSingleRes() {
      let formData = new FormData(); 
      var Resume = document.getElementById("resfile").files[0]

      formData.append("file", Resume);
      var alpha = []
      for (var i in skillsname){
        var temp = document.getElementById("pa"+i.toString())
        alpha.push(temp.value)
      }
      console.log(alpha)
      formData.append("skillsalpha","["+alpha.toString()+"]")
      console.log(alpha.toString())
      formData.append("skillsvec",JSON.stringify(skillsvec))
      await fetch('/computessingle', {
        method: "POST", 
        body: formData
      }).then(response =>{
        response.json().then(
          res =>{
            console.log(res.Rank)
            console.log(res["Rank"])
            alert('resume Rank : '+res.Rank.toString())
          }
        )
      }); 
      }
      async function getMultiple() {
        let formData = new FormData(); 
        var Resume = document.getElementById("resfile").files[0]
  
        formData.append("file", Resume);
        var alpha = []
        for (var i in skillsname){
          var temp = document.getElementById("pa"+i.toString())
          alpha.push(temp.value)
        }
        console.log(alpha)
        formData.append("skillsalpha","["+alpha.toString()+"]")
        console.log(alpha.toString())
        formData.append("skillsvec",JSON.stringify(skillsvec))
        await fetch('/computemultiple', {
          method: "POST", 
          body: formData
        }).then(response =>{
          //console.log(response.json())

          response.json().then(resp =>{
            console.log(resp)
            console.log(resp)
            var resume1 = resp.Resume
            var score1 = resp.Scores
            var arr1 = []
            for(var i in resume1){
              var name = resume1[i]
              var score = score1[i]
              var temp2 = new Data(name,score)
              arr1.push(temp2)
            }
            arr1.sort(function(a,b){
              return b.score - a.score;
            })
            for(var i in arr1){
              console.log(arr1[i].score)
            }
            for(var i in arr1){
              var ele = document.getElementById("multians")
              var temp1 = document.createElement("p")
              temp1.innerText = arr1[i].name
              var temp2 = document.createElement("p")
              temp2.innerText = arr1[i].score
              ele.appendChild(temp1)
              ele.appendChild(temp2)
            }
          })
          //alert('The file has been uploaded successfully.')
        }); 
        }
  
    /*
      async function uploadJD() {
        let formData = new FormData(); 
        var jdfile = document.getElementById("jdfile").files[0]
  
        formData.append("file", jdfile);
        await fetch('/jdupload', {
          method: "POST", 
          body: formData
        }); 
        alert('The file has been uploaded successfully.');
        }
        */
       async function uploadJD(){
          var jd = document.getElementById("jdfile")
          var formData = new FormData()
          formData.append("file",jd.files[0])

          await fetch("/jdupload",{
            method : "POST",
            body : formData
          }).then(response =>{
              response.json().then(resp => {
                console.log(resp)
                skillsname = resp.skillsname
                skillsvec = JSON.parse(resp.skillsvec)
                console.log("===")
                console.log(skillsname)
                console.log(skillsvec)
                var parent = document.getElementById("params11")

                for(var i in skillsname){
                  console.log("Parent",parent)
                  var name = skillsname[i]
                  console.log(i)
                  var ele = document.createElement("input")
                  ele.type = "number"
                  ele.id = "pa"+i.toString()
                  skillsid.push(ele.id)
                  var ele2 = document.createElement("p")
                  ele2.innerHTML = name
                  //ele.placeholder = name
                  parent.appendChild(ele2)
                  parent.appendChild(ele)
                }
              })
          }).catch(err =>console.log(err))
       }

       async function uploadZipfile() {
        let formData = new FormData(); 
        var Resume = document.getElementById("zipfile").files[0]
  
        formData.append("file", Resume);
        await fetch('/zipupload', {
          method: "POST", 
          body: formData
        }).then(
          resp =>{
            
            console.log(resp)
          }
        ); 
        
        }
  
  
  

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