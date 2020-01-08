/*Autor: Edmundo Ribeiro 
  Email: jtvedy@gmail.com / edmundoribeiro@mecajun.com

  Código interpretado pelo photoshop para criação de 
  assisnaturas de email no formato .jpeg conforme dados 
  numa planilha no drive

*/
#include json2.js

(function main(){
	var membros = loadJson('membros.json');
	alert(membros.length);
	for(var i = 0; i < membros.length; i++){
		processMember(membros[i]);
	}
})();

function processMember(membro){

	var nameLayer = app.activeDocument.layerSets.getByName('Nome').layers[0];
	var roleLayer = app.activeDocument.layerSets.getByName('Cargo').layers[0];
	var phoneLayer = app.activeDocument.layerSets.getByName('Telefone').layers[0];


	nameLayer.textItem.contents = membro.name;
	roleLayer.textItem.contents = membro.role;
	phoneLayer.textItem.contents = membro.phone;
	saveJpeg(membro.name);
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
	var file = new File(doc.path + '/assinaturas/' + name + '.jpg');
	var opts = new JPEGSaveOptions();
	opts.quality = 10;

	doc.saveAs(file, opts, true);
	
}