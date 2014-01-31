define([
    'jquery', 
    'underscore',
    'backbone', 
    'text!templates/common/index.html',
], function($, _, Backbone, Index){
    var IndexView = Backbone.View.extend({
	render: function(data){
	    $('#content').html(_.template(Index, data));	    
	},
    });			 
    return IndexView;
});