/*Author: Edmundo Ribeiro 
  Email: jtvedy@gmail.com / edmundoribeiro@mecajun.com



*/
#include "libraries/json2.js"

var data_file = 'members.json';
var output_folder = 'Signatures';

(function main(){
	var members = loadJson(data_file);
	alert(members.length + ' Members');
	for(var i = 0; i < members.length; i++){
		processMember(members[i]);
	}
})();

function processMember(member){

	var nameLayer = app.activeDocument.layerSets.getByName('Name').layers[0];
	var roleLayer = app.activeDocument.layerSets.getByName('Role').layers[0];
	var phoneLayer = app.activeDocument.layerSets.getByName('Phone').layers[0];


	nameLayer.textItem.contents = member.name;
	roleLayer.textItem.contents = member.role;
	phoneLayer.textItem.contents = member.phone;
	saveJpeg(member.name);
}

function loadJson(relPath){
	var script = new File($.fileName);
	var jsonFile = new File(script.path + '/' + relPath);

	jsonFile.open();
	var str = jsonFile.read();
	jsonFile.close();

	return JSON.parse(str);
}

function saveJpeg(name){
	var doc = app.activeDocument;
	var file = new File(doc.path + '/' + output_folder + '/' + name + '.jpg');
	var opts = new JPEGSaveOptions();
	opts.quality = 10;

	doc.saveAs(file, opts, true);
	
}