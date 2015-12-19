/* Javascript sheet */

function runSidebar() {
	$(document).ready(function() {
		$('#sidebar').simpleSidebar({
			opener: '#button',
      wrapper: '#wrapper',
	    sidebar: {
	       align: 'left', //or 'right' - This option can be ignored, the sidebar will automatically align to right.
         width: 300, //You can ignore this option, the sidebar will automatically size itself to 300px.
         closingLinks: '.close-sidebar' // If you ignore this option, the plugin will look for all links and this can be buggy. Choose a class for every object inside the sidebar that once clicked will close the sidebar.
         css: {
           //Here you can add more css rules but you should use your own stylesheet.
           zIndex: 3000 //Choose the amount of zIndex you want. It must be the higher zIndex number.
         }
       }
     });
   });
}