//TODO add cache variable for close button for all divs
//TODO add plain background for img showing nothing in the beginning
//TODO add timeout to clear all imgs in folder at the end of the day
//TODO add snackbar to show that the model is ready to display

var socket = io.connect();
var worldsNumber;
var propsNumber;

var val = {};
var expectations = {};
var valList = [];
var valNumber = 0;

var rel = {};
var relList = [];
var relNumber = 0;

var clientid = '';

var target = '';
var targetFile = '';

var modelWorld = 0;
var modelFormula = '';


//HTML changes for Generate button
function createTable()
{
	//get values of number of worlds and propositions
	worldsNumber = document.getElementById("worldsNum").value;
	propsNumber = document.getElementById("propsNum").value;
	
	//create html checkbox tables for the three modify buttons
    var theader = '<table class="mdl-data-table mdl-js-data-table">\n';
    
    var theadBegin = '<thead>\n<tr>\n<th></th>\n';
    var theadBody = '';
    for (i=0;i<propsNumber;i++) {
    	theadBody += '<th>P'+i.toString() + '</th>\n';
    }
    var theadEnd = '</tr>\n</thead>\n'; 
    
    var tbodyBegin = '<tbody>\n';
    var tbodyBody = '';
    var counter = 0;
    for( var i=0; i<worldsNumber;i++)
    {
        tbodyBody += '<tr>\n';
        	tbodyBody += '<td>w'+ i.toString() +'</td>';
        	for (j=1;j<=propsNumber;j++) {
        		tbodyBody += '<td>';
        		tbodyBody += '<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="valuation-'+ i.toString() + '-' + counter.toString() +'">\n<input type="checkbox" id="valuation-'+ i.toString() + '-' + counter.toString() +'" class="mdl-checkbox__input">\n</label>\n';
        		tbodyBody += '</td>\n';
        		counter = counter + 1;
        	}
        counter = 0;
        tbodyBody += '</tr>\n';
    }
    var tbodyEnd = '</tbody>\n';
    
    var tfooter = '</table>\n';
    
    ////////////////////////////////////////////////////////////////////////////////
    
    var theadBegin1 = '<thead>\n<tr>\n<th></th>\n';
    var theadBody1 = '';
    for (i=0;i<worldsNumber;i++) {
    	theadBody1 += '<th>w'+i.toString() + '</th>\n';
    }
    var theadEnd1 = '</tr>\n</thead>\n';
    
    var tbodyBegin1 = '<tbody>\n';
    var tbodyBody1 = '';
    for( var i=0; i<worldsNumber;i++)
    {
        tbodyBody1 += '<tr>\n';
        	tbodyBody1 += '<td>w'+ i.toString() +'</td>';
        	for (j=0;j<worldsNumber;j++) {
        		tbodyBody1 += '<td>';
        		tbodyBody1 += '<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="relation-'+ i.toString() + '-' + j.toString() +'">\n<input type="checkbox" id="relation-'+ i.toString() + '-' + j.toString() +'" class="mdl-checkbox__input">\n</label>\n';
        		tbodyBody1 += '</td>\n';
        	}
        tbodyBody1 += '</tr>\n';
    }
    var tbodyEnd1 = '</tbody>\n';

	//////////////////////////////////////////////////////////////////////////////////
    
    var theadBegin2 = '<thead>\n<tr>\n<th>WORLDS</th>\n<th>EXPECTATIONS</th>\n</tr>\n</thead>\n';
    
    var tbodyBegin2 = '<tbody>\n';
    var tbodyBody2 = '';
    for (var i=0; i<worldsNumber;i++) {
    	tbodyBody2 += '<tr>\n';
    	tbodyBody2 += '<td>w'+ i.toString() +'</td>\n<td>\n';
    	tbodyBody2 += '<form action="#">\n';
		  tbodyBody2 += '<div class="mdl-textfield mdl-js-textfield">\n';
		  tbodyBody2 += '<input class="mdl-textfield__input" type="text" id="expectation-'+ i.toString() +'">\n';
		  tbodyBody2 += '<label class="mdl-textfield__label" for="expectation-'+ i.toString() +'"></label>\n';
		  tbodyBody2 += '</div>\n';
		  tbodyBody2 += '</form>\n';
    	tbodyBody2 += '</td>\n';
    	tbodyBody2 += '</tr>\n';
    }
    var tbodyEnd2 = '</tbody>\n';
    
    document.getElementById('wrapper').innerHTML = theader + theadBegin + theadBody + theadEnd + tbodyBegin + tbodyBody + tbodyEnd + tfooter;
    
    document.getElementById('wrapper1').innerHTML = theader + theadBegin1 + theadBody1 + theadEnd1 + tbodyBegin1 + tbodyBody1 + tbodyEnd1 + tfooter;
    
    document.getElementById('wrapper2').innerHTML = theader + theadBegin2 + tbodyBegin2 + tbodyBody2 + tbodyEnd2 + tfooter;
    
    var position = '';
    for (var i=0; i<worldsNumber;i++) {
    	var stri = i.toString();
    	position = 'relation-'+ stri +'-'+ stri;
    	var reflexiveCheckbox = document.getElementById(position);
    	reflexiveCheckbox.checked = true;
    	document.getElementById(position).disabled = true;
    }
}

//dialog boxes for the modify buttons which will display the checkbox tables
  (function() {
    'use strict';
    var dialogButton = document.querySelector('.dialog-button1');
    var dialog = document.querySelector('#dialog1');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    dialogButton.addEventListener('click', function() {
       dialog.showModal();
    });
    dialog.querySelector('button:not([disabled])')
    .addEventListener('click', function() {
      dialog.close();
    });
  }());
  
    (function() {
    'use strict';
    var dialogButton = document.querySelector('.dialog-button2');
    var dialog = document.querySelector('#dialog2');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    dialogButton.addEventListener('click', function() {
       dialog.showModal();
    });
    dialog.querySelector('button:not([disabled])')
    .addEventListener('click', function() {
      dialog.close();
    });
  }());

(function() {
    'use strict';
    var dialogButton = document.querySelector('.dialog-button');
    var dialog = document.querySelector('#dialog');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    dialogButton.addEventListener('click', function() {
       dialog.showModal();
    });
    dialog.querySelector('button:not([disabled])')
    .addEventListener('click', function() {
      dialog.close();
    });
  }());
  
function closeModal() {
	document.querySelector('#dialog').close();
}
function closeModal1() {
	document.querySelector('#dialog1').close();
}
function closeModal2() {
	document.querySelector('#dialog2').close();
}


function makeSym() {
	var stri;
	var strj;
	var positionij = '';
	var positionji = '';
	var ijBox;
	var jiBox;
	for (var i=0; i<worldsNumber; i++) {
		for (var j=0; j<worldsNumber; j++) {
			if (i!==j) {
				stri = i.toString();
				strj = j.toString();
				positionij = 'relation-'+stri+'-'+strj;
				positionji = 'relation-'+strj+'-'+stri;
				ijBox = document.getElementById(positionij);
				jiBox = document.getElementById(positionji);
				if (ijBox.checked === true || jiBox.checked === true) {
					ijBox.checked = true;
					jiBox.checked = true;
				}
			}
		}
	}
}

function makeTran() {
	var stri;
	var strj;
	var strk;
	var positionij = '';
	var positionik = '';
	var positionkj = '';
	var ijBox;
	var ikBox;
	var kjBox;
	for (var k=0; k<worldsNumber; k++) {
		for (var i=0; i<worldsNumber; i++) {
			for (var j=0; j<worldsNumber; j++) {
				stri = i.toString();
				strj = j.toString();
				strk = k.toString();
				positionij = 'relation-'+stri+'-'+strj;
				positionik = 'relation-'+stri+'-'+strk;
				positionkj = 'relation-'+strk+'-'+strj;
				ijBox = document.getElementById(positionij);
				ikBox = document.getElementById(positionik);
				kjBox = document.getElementById(positionkj);
				ijBox.checked = ijBox.checked || (ikBox.checked && kjBox.checked);
			}
		}
	}
}

function modelChecker() {
	modelWorld = document.getElementById('modelWorld').value;
	modelFormula = document.getElementById('modelFormula').value;
	socket.emit('modelCheckerInput', {world:worldsNumber,prop:propsNumber,valuation:valNumber, relation:relNumber, checkWorld:modelWorld, checkFormula:modelFormula});
}

/////////////////////////////////////////////////SERVER INTERACTION FOR PYTHON////////////////////////////////////////////////////////////

socket.on('sendID', function(data) {
	clientid = data.ID;
});


//create Empty Model when generate is clicked
function emptyModel() {
	socket.emit('emptyModel', {world:worldsNumber, prop:propsNumber});
};
socket.on('emptyModelCreated', function(data){
	targetFile = data.src;
});
function displayModel() {
	target = "imgs/"+ targetFile +".png"
	document.getElementById('imgPane').src = target;
};

//when save button is clicked on valuation checkbox table
function saveValuation() {
	valList = [];
	for (var i=0; i<worldsNumber;i++) {
		val[i] = [];
		for (var j=0; j<propsNumber;j++) {
			position = "valuation-" + i + "-" + j;
			if (document.getElementById(position).checked == true) {
				val[i].push(j);
				valList.push(1);
			} else {
				valList.push(0);
			}
		}
		
	}
	valNumber = valList.join("");
	relList = [];
	for (var i=0; i<worldsNumber;i++) {
		rel[i] = [];
		for (var j=0; j<worldsNumber;j++) {
			position = "relation-" + i + "-" + j;
			if (document.getElementById(position).checked == true) {
				rel[i].push(j);
				relList.push(1);
			} else {
				relList.push(0);
			}
		}
		
	}
	relNumber = relList.join("");
	console.log(relNumber);
	console.log(valNumber);
	socket.emit('nonEmptyModelUpdated',{world:worldsNumber,prop:propsNumber,valuation:valNumber, relation:relNumber});
};


socket.on('modelUpdated', function(data) {
	targetFile = data.src;
});





