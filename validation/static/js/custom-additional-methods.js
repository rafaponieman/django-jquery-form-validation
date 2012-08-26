// Custom method to parse regular expressions
// that are strings instead of JS native RegExp objects.
// This is because Django renders the json dictionary and
// it can't 

jQuery.validator.addMethod("regexp", function(a,b,c){
	return this.optional(b)||new RegExp(c).test(a);
}, "Invalid format.");
