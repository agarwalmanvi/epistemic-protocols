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

var worldsNumber;
var propsNumber;

function readInput() {
	worldsNumber = document.getElementById("worldsNum").value;
	propsNumber = document.getElementById("propsNum").value;
}

function createTable()
{
    var theader = '<table class="mdl-data-table mdl-js-data-table">\n';
    
    var theadBegin = '<thead>\n<tr>\n<th></th>\n';
    var theadBody = '';
    for (i=1;i<=propsNumber;i++) {
    	theadBody += '<th>P'+i.toString() + '</th>\n';
    }
    var theadEnd = '</tr>\n</thead>\n'; 
    
    var tbodyBegin = '<tbody>\n';
    var tbodyBody = '';
    var counter = 1;
    for( var i=1; i<=worldsNumber;i++)
    {
        tbodyBody += '<tr>\n';
        	tbodyBody += '<td>w'+ i.toString() +'</td>';
        	for (j=1;j<=propsNumber;j++) {
        		tbodyBody += '<td>';
        		tbodyBody += '<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="valuation-'+ counter.toString() +'">\n<input type="checkbox" id="valuation-'+ counter.toString() +'" class="mdl-checkbox__input">\n</label>\n';
        		tbodyBody += '</td>\n';
        		counter = counter + 1;
        	}
        tbodyBody += '</tr>\n';
    }
    var tbodyEnd = '</tbody>\n';
    
    var tfooter = '</table>\n';
    
    var theadBegin1 = '<thead>\n<tr>\n<th></th>\n';
    var theadBody1 = '';
    for (i=1;i<=worldsNumber;i++) {
    	theadBody1 += '<th>w'+i.toString() + '</th>\n';
    }
    var theadEnd1 = '</tr>\n</thead>\n';
    
    var tbodyBegin1 = '<tbody>\n';
    counter = 1;
    var tbodyBody1 = '';
    for( var i=1; i<=worldsNumber;i++)
    {
        tbodyBody1 += '<tr>\n';
        	tbodyBody1 += '<td>w'+ i.toString() +'</td>';
        	for (j=1;j<=worldsNumber;j++) {
        		tbodyBody1 += '<td>';
        		tbodyBody1 += '<label class="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect" for="relation-'+ counter.toString() +'">\n<input type="checkbox" id="relation-'+ counter.toString() +'" class="mdl-checkbox__input">\n</label>\n';
        		tbodyBody1 += '</td>\n';
        		counter = counter + 1;
        	}
        tbodyBody1 += '</tr>\n';
    }
    var tbodyEnd1 = '</tbody>\n';
    
    var theadBegin2 = '<thead>\n<tr>\n<th>WORLDS</th>\n<th>EXPECTATIONS</th>\n</tr>\n</thead>\n';
//    var theadBody2;
//    var theadEnd2;
    
    var tbodyBegin2 = '<tbody>\n';
    var tbodyBody2 = '';
    for (var i=1; i<=worldsNumber;i++) {
    	tbodyBody2 += '<tr>\n';
    	tbodyBody2 += '<td>w'+ i.toString() +'</td>\n<td>\n';
    	tbodyBody2 += '<form action="#">\n';
		  tbodyBody2 += '<div class="mdl-textfield mdl-js-textfield">\n';
		  tbodyBody2 += '<input class="mdl-textfield__input" type="text" id="sample'+ i.toString() +'">\n';
		  tbodyBody2 += '<label class="mdl-textfield__label" for="sample'+ i.toString() +'"></label>\n';
		  tbodyBody2 += '</div>\n';
		  tbodyBody2 += '</form>\n';
    	tbodyBody2 += '</td>\n';
    	tbodyBody2 += '</tr>\n';
    }
    var tbodyEnd2 = '</tbody>\n';
    
    document.getElementById('wrapper').innerHTML = theader + theadBegin + theadBody + theadEnd + tbodyBegin + tbodyBody + tbodyEnd + tfooter;
    
    document.getElementById('wrapper1').innerHTML = theader + theadBegin1 + theadBody1 + theadEnd1 + tbodyBegin1 + tbodyBody1 + tbodyEnd1 + tfooter;
    
    document.getElementById('wrapper2').innerHTML = theader + theadBegin2 + tbodyBegin2 + tbodyBody2 + tbodyEnd2 + tfooter;
}


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



