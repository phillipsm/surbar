var file_names = ['camomile', 'chartographist', 'cornutine', 'petalody', 'asci', 'bescorch', 'cephalology', 'coset', 'dawning', 'ideogenous', 'ingluviitis', 'interchangeable', 'pentlandite', 'plagium', 'rebilling', 'transaquatic', 'unpoetize', 'adzooks', 'buggery', 'connectional', 'deheathenize', 'enderon', 'familiar', 'grudge', 'indentment', 'ragtag', 'splotchy', 'thumbprint', 'unanimistic', 'catalectic', 'concretional', 'hiccup', 'souchong', 'eurythmics', 'salvarsan', 'acylate', 'complication', 'enwoman', 'eros', 'limer', 'lorate', 'patas', 'pore', 'predisclosure', 'schoolless', 'triakisoctahedron', 'unaugmented', 'ungeological', 'aphelops', 'decare', 'ethicize', 'redbait', 'afrikander', 'agy', 'airliner', 'anorth', 'beau', 'bespeckle', 'biunivocal', 'broadwife', 'contemporaneousness', 'cueva', 'cystoptosis', 'dacelonine', 'demiditone', 'disfrock', 'enplane', 'euphony', 'fencible', 'grisaille', 'implementiferous', 'increately', 'incremate', 'inobedience', 'juvenalian', 'labba', 'matriarchate', 'melanterite', 'mischarge', 'myriacanthous', 'nonreimbursement', 'osteocele', 'polypheme', 'populin', 'postcephalic', 'posthetomist', 'saponacity', 'scooped', 'sericulture', 'sesquiquintile', 'sprucery', 'subgular', 'swagger', 'trombidiidae', 'uncorruptly', 'underclub', 'undermist', 'underquote', 'unexpectant', 'unflead', 'unfounded', 'unmullioned', 'unrelaxing', 'vaginotome', 'wolver', 'armangite', 'desyatin', 'fisheye', 'neologize', 'paddlelike', 'parsimonious', 'allalinite', 'byrewards', 'crag', 'creole', 'deaner', 'disconnectedness', 'drongo', 'hypocytosis', 'melanocomous', 'molysite', 'oatenmeal', 'salite', 'soredium', 'velellidous', 'waltzlike', 'abridgeable', 'aforethought', 'anagua', 'beech', 'cajuela', 'chrysotis', 'ciliotomy', 'congratulate', 'daring', 'disciplinatory', 'distensibility', 'drewite', 'encyclopedism', 'fireflower', 'fixedness', 'freeholder', 'gustativeness', 'homophyllous', 'hostilize', 'immethodize', 'intercohesion', 'jackanapish', 'korntunnur', 'leersia', 'maitlandite', 'more', 'oxygenizable', 'paleoatavistic', 'perceptually', 'prevalent', 'receivedness', 'resthouse', 'strayaway', 'supercorporation', 'swahilian', 'tidehead', 'trapper', 'unprejudicedness', 'willmaker', 'xanthoceras', 'aluminish', 'digitipinnate', 'balloonist', 'woodbine', 'aqueduct', 'favorer', 'harborless', 'highbred', 'paly', 'prune', 'tormentous', 'campbellite', 'concher', 'goatbeard', 'indraft', 'linon', 'mesomeric', 'nettie', 'quinarian', 'rackettail', 'servitude', 'aegialitis', 'akeley', 'angiokeratoma', 'anhydromyelia', 'architectonic', 'bilirubinic', 'bolter', 'cyclopentene', 'dinothere', 'dyserethisia', 'fishhooks', 'fluorogenic', 'foresummon', 'gramophonically', 'gravidity', 'grievance', 'grillroom', 'histogenesis', 'hypothenal', 'lied', 'lithosian', 'marble', 'mesodevonian', 'nongelatinizing', 'omniscribent', 'parenthesis', 'percussion', 'pohutukawa', 'popolari', 'progesterone', 'quinquepedal', 'ruddily', 'saint', 'savonarolist', 'soldierliness', 'spraints', 'stingfish', 'stopwater', 'subdecuple', 'subtrahend', 'tacahout', 'tachygenesis', 'timbered', 'unacquaintance', 'undergraduatish', 'accipitres', 'balt', 'ephemeran', 'kinkcough', 'relatedness', 'subvirate', 'toponarcosis', 'ungulp', 'vady', 'wurzel', 'abeltree', 'admonitorial', 'aminobenzene', 'antiphysical', 'ardennite', 'axminster', 'baldy', 'basidiophore', 'blandfordia', 'bluegrass', 'busker', 'calochortaceae', 'catena', 'cephalometry', 'chylidrosis', 'contrafagotto', 'convincibility', 'corporational', 'cotoin', 'didymia', 'drammage', 'dumpishly', 'enterostasis', 'fantasia', 'flogmaster', 'foreordainment', 'freit', 'galligaskin', 'gorger', 'heathen', 'hemianesthesia', 'histomorphological', 'hypoglycemia', 'juxtapyloric', 'monoganglionic', 'nematode', 'nicolaitan', 'peptonization', 'periphlebitic', 'pleomorphic', 'plumelike', 'prodeportation', 'protoma', 'reformingly', 'seetulputty', 'shagginess', 'signify', 'spencerianism', 'superendow', 'supermedial', 'tillotter', 'umbrosity', 'uncommitted', 'unveiler', 'viner', 'zoograft', 'algernon', 'depriver', 'dioestrous', 'extrapolative', 'jackaroo', 'langsdorffia', 'megachilidae', 'micropore', 'naharvali', 'nominature', 'renovatory', 'revelability', 'simarouba', 'aforesaid', 'aphthic', 'boshas', 'celestine', 'centrarchoid', 'chitinized', 'coolie', 'intelligencer', 'stench', 'friarhood', 'halerz', 'intralocular', 'mantid', 'stereometer', 'unrepiningly', 'archispore', 'choreomania', 'fillock', 'krama', 'perforant', 'phthalein', 'serdar', 'urochromogen', 'whininess'];
var recently_displayed = [];

var name = file_names[Math.floor(Math.random()*file_names.length)];
var interval;

function load_censored() {

	// we don't want to repeat in a small time span
	name = file_names[Math.floor(Math.random()*file_names.length)];
	while (recently_displayed.indexOf(name) >= 0) {
		name = file_names[Math.floor(Math.random()*file_names.length)];		
	}

	recently_displayed.push(name);
	if (recently_displayed.length === file_names.length/2) {
		recently_displayed.pop();
	}

	// we have our name, let's swap it out with what's currently displayed
	$('.image-container').each(function (index, value) {
		$(this).fadeToggle(40, function() {
			$('<img src="../scripts/data/processed/' + name + '.png" />'); // preload the image
			$(this).children('img').attr('src', '../scripts/data/processed/' + name + '.png');
			$(this).children('span').html(name);
			$(this).fadeToggle(40);
			clearInterval(interval);
			interval = window.setInterval(load_censored, 8000);
  		});
	});
}

$(document).ready(function() {
	load_censored();
});

$(document).keypress(function(e) {
	load_censored()
});