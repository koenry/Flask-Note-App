
let valueText = 'ok';
let valueText2 = 'ok';
const serverName = '127.0.0.1';
let username = 'user'
// main fetch

let saveHtml = ''
const sendFetchReq = () => {
  fetch(`http://${serverName}:5000/postmethod`, {
  method: 'POST',
  body: JSON.stringify(saveHtml),
  headers: new Headers({
    'Content-Type': 'application/json'
  })
})
}

// upload image func
const uploadImage = () => {

  let id = this.document.activeElement.getAttribute("id")
  let id2 = id.substring(0, id.length - 1 )+'aa'
  let id3 = id.substring(0, id.length - 1)
  let path = document.getElementById(id3+'e').value.split("\\").pop()

  fetch(`http://${serverName}:5000/getuserdir`, {
  method: 'POST',
  body: JSON.stringify(path),
  headers: new Headers({
    'Content-Type': 'application/json'
  })
})
fetch(`http://${serverName}:5000/getuserdir2`)
  .then(res => res.json())
  .then(data5 => { 
      path = data5[0]
  if(path.endsWith('.png') || path.endsWith('.jpg') || path.endsWith('.jpeg')) {    
      const photoElem = document.createElement("img");
      photoElem.className = 'gridImg';
      photoElem.id = id+'k';
      photoElem.src = `http://127.0.0.1:5000/static/filestorage/${data5[1]}/${path}`
      document.getElementById(id2).appendChild(photoElem);
      saveHtml = document.documentElement.outerHTML;
      sendFetchReq()
      alert('File Uploaded')
      location.reload()    
  }
  else {
    alert('Please select an image!')
    location.reload()
  }
})
}

 // change pw
 document.getElementById("changePw").onclick = function(){
    
  window.open("http://127.0.0.1:5000/changepw","_self")
}

// delete func
const deleteFunc = () => {
  const deletingElem = event.target.id.substring(0, event.target.id.length - 1);
  const comfirmation = confirm("Are you sure you want to the note?");
  if (comfirmation == true) {
    document.getElementById(deletingElem).remove();
    document.getElementById(deletingElem+'a').remove();
    document.getElementById(deletingElem+'b').remove();
    document.getElementById(deletingElem+'c').remove();
    document.getElementById(deletingElem+'d').remove();
    
    // check if an iamge is uploaded or not
    if(document.getElementById(deletingElem+'dk')) {
      document.getElementById(deletingElem+'dk').remove();
      document.getElementById(deletingElem+'aa').remove();
      
    }
    saveHtml = document.documentElement.outerHTML;
    sendFetchReq()
    alert('Deleted!')
  } 
}
// edit func for created note
const editFunc = () => {
    valueText = event.target.id.substring(0, event.target.id.length - 1)+'a'; // save the id we're editing to a variable 
    valueText2 = event.target.id.substring(0, event.target.id.length - 1);
    let titleValue = document.getElementById(event.target.id.substring(0, event.target.id.length - 1)).textContent;
    let editValue = document.getElementById(event.target.id.substring(0, event.target.id.length - 1)+'a').textContent;
    // I  gave each new elements new ids+a number so we delete the last number and add a 2 to get the correct one
  
    // blur other elements
    document.getElementById("grid-container2").style.filter = "blur(0.5rem)";
    document.getElementById("gridAdd-container").style.filter = "blur(0.5rem)";
    document.getElementById("categoryBoxEdit").style.display = "block";
    document.getElementById("categoryBoxEditButton").style.display = "block";
    document.getElementById("categoryBoxEditButton2").style.display = "block";
    document.getElementById("titleBoxEdit").style.display = "block";
    document.getElementById('categoryBoxEdit').value = editValue;
    document.getElementById('titleBoxEdit').value = titleValue;
    document.getElementById("categoryBoxEdit").focus();
}


const save = document.getElementById("btnSave");
save.addEventListener("click", mainFunc);

function mainFunc() {
  // getText is going to be used for manipulating unique ids
  // getTextDuplicate is for the original text input 
  let getText = document.getElementById("categoryBox").value;
  let getTextDuplicate = document.getElementById("categoryBox").value;
  let getText2 = document.getElementById("categoryBox2").value;
  const mainFunc2 = () => {
    
    // this is our random id generator if the user has a duplicate id.
    const randomId = Math.floor(Math.random() * 10000000);
    if (document.body.contains(document.getElementById(getText)) == true ) {
      getText = getText + String(randomId);
         
    }
    
    const element = document.createElement("div");
    element.className = 'gridAdd-item';
    element.innerText = getTextDuplicate;
    element.id = getText
    const parent  = document.getElementById('gridAdd-container');
    parent.appendChild(element);

    const element2 = document.createElement("div");
    element2.className = 'gridAdd-item2';
    element2.innerText = getText2;
    element2.id = getText+'a';
    parent.appendChild(element2);

    const element22 = document.createElement("div");
    element22.className = 'gridAdd-item22';
    element22.id = getText+'aa';
    parent.appendChild(element22);

    const elementBtnDiv = document.createElement("div");
    elementBtnDiv.className = 'gridAdd-item2';
  // I have added a letter to each element because we cannot have duplicate ids
    elementBtnDiv.id = getText+'d';
    parent.appendChild(elementBtnDiv);
    const parent2  = document.getElementById(getText+'d'); // add buttons to newly created divs

    const element4 = document.createElement("button");
    element4.className = 'gridAdd-item4';
    element4.innerText = 'Edit';  
    element4.id = getText+'b';
    
    parent2.appendChild(element4);

    // edit option
    element4.onclick = function() {
      editFunc();
    }
    
  
    const element3 = document.createElement("button");
    element3.className = 'gridAdd-item3';
    element3.innerText = 'Delete';  
    element3.id = getText+'c';
    parent2.appendChild(element3);

    // delete option
    element3.onclick = function() {
      deleteFunc()
    }
    // upload option
    const elementUpload = document.createElement("FORM");
    elementUpload.name='myForm';
    elementUpload.method='POST';
    elementUpload.action='/login'
    
    elementUpload.enctype='multipart/form-data';
    parent2.appendChild(elementUpload)

    const elementInput =document.createElement('INPUT');
    elementInput.type='file';
    elementInput.name='image';
    elementInput.id = getText+'e';
    elementUpload.appendChild(elementInput);

    const elementSubmitBtn = document.createElement('button');
    elementSubmitBtn.type='FILE';
    elementSubmitBtn.name='image';
    elementSubmitBtn.innerText = 'Upload'; 
    elementSubmitBtn.className ='uploadSubmitBtn';
    elementSubmitBtn.id = getText+'d';
    elementUpload.appendChild(elementSubmitBtn);
    elementSubmitBtn.onclick = function() {
      uploadImage()
      }
    

    elementUpload.id = getText+'c';
    parent2.appendChild(elementUpload);
    
    saveHtml = document.documentElement.outerHTML;
    sendFetchReq() 
    document.getElementById('categoryBox').value='';
    document.getElementById('categoryBox2').value='';
    alert('Note created!');
    }
     // test for null inputs from the user
    if ( getText2 == '' || getText == ''){
      alert("Title and/or text can't be empty!");
    }
    else {
      mainFunc2()
    }
  }

  // edit button functions :exit :save for after you open note editor

  document.getElementById("categoryBoxEditButton").onclick = function(){
    document.getElementById(valueText).innerText = document.getElementById('categoryBoxEdit').value;
    document.getElementById(valueText2).innerText = document.getElementById('titleBoxEdit').value;
    document.getElementById("categoryBoxEdit").style.display = "none";
    document.getElementById("categoryBoxEditButton").style.display = "none";
    document.getElementById("categoryBoxEditButton2").style.display = "none";
    document.getElementById("titleBoxEdit").style.display = "none";
    document.getElementById("grid-container2").style.filter = "blur(0rem)";
    document.getElementById("gridAdd-container").style.filter = "blur(0rem)";
    saveHtml = document.documentElement.outerHTML;
    sendFetchReq()
    };

  document.getElementById("categoryBoxEditButton2").onclick = function(){
    document.getElementById("categoryBoxEdit").style.display = "none";
    document.getElementById("categoryBoxEditButton").style.display = "none";
    document.getElementById("categoryBoxEditButton2").style.display = "none";
    document.getElementById("titleBoxEdit").style.display = "none";
    document.getElementById("grid-container2").style.filter = "blur(0rem)";
    document.getElementById("gridAdd-container").style.filter = "blur(0rem)";
  };
  // logout
  document.getElementById("logout").onclick = function(){
    window.open(`http://${serverName}:5000/logout`,"_self")
  }
 
  // check if id does not exists, so if the user creates a duplicate title he wont delete both of them when deleting

// Because after each creation we only then add an event 
// So the user can only delete and edit on the same session
// With queryselectorall we make it so that it selects every already created elements and gives them the same on click effect

const queryAllEdit = document.querySelectorAll('.gridAdd-item4');
queryAllEdit.forEach(el => el.addEventListener('click', event => {
  editFunc(); 
}));

const queryAllDelete = document.querySelectorAll('.gridAdd-item3');
queryAllDelete.forEach(el => el.addEventListener('click', event => {
  deleteFunc()
}));

const uploadSubmitBtn = document.querySelectorAll('.uploadSubmitBtn');
uploadSubmitBtn.forEach(el => el.addEventListener('click', event => {
  uploadImage()
}));


