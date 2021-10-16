/*!
* Start Bootstrap - Business Frontpage v5.0.4 (https://startbootstrap.com/template/business-frontpage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

jQuery(document).ready(function () {
    FooterPosition();

    jQuery(window).resize(function () {
        FooterPosition();
    });
});

var originalFooterBottom = 0;

function FooterPosition() {
    var windowHeight = jQuery(window).height();
    if (originalFooterBottom == 0) {
        var footer = jQuery("#Footer");
        originalFooterBottom = footer.position()['top'] + footer.height();
    }

    if (windowHeight > originalFooterBottom) {
        var footerElement = document.getElementById("Footer");
        if (!footerElement.classList.contains('FooterBottom')) {
            footerElement.classList.add('FooterBottom');
        }
    }
    else {
        var footerElement = document.getElementById("Footer");
        if (footerElement.classList.contains('FooterBottom')) {
            footerElement.classList.remove('FooterBottom');
        }
    }



var spinner;
jQuery(function(){
    spinner = new Spinner().spin().el;
    jQuery(document.body).append(spinner);
    jQuery(spinner).css('display','none');
});

window.onbeforeunload = function(e){
    if(e != null && e != undefined){
        jQuery(spinner).css('display','');
    }
};