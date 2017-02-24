

function animateElems() {
    // define element variables
    var e1 = $('.info1');
    var e2 = $('.info2');
    var e3 = $('.info3');
    var e4 = $('.info4');

    // define animation sequence
    var sequence = [{
      e: e1,
      p: 'fadeIn',
      o: {


        }
    }, {
        e: e2,
        p: 'fadeIn',
        o: {
            stagger:200 , drag: true,
        }
    }, {
      e: e3,
      p: 'fadeIn',
      o: {
         stagger:200 , drag: true,

        }
    },
    {
      e: e4,
      p: 'fadeIn',
      o: {
         stagger:200 , drag: true,

        }
    },
    ];

    // run animation sequence
    $("#about").waypoint(function() {
      $.Velocity.RunSequence(sequence);
    }, { offset: '50%'});
}


$( document ).ready(function() {
  $(".info1").velocity({ opacity: 0 });
  $("#fact1").velocity({ opacity: 0 });
  $("#fact2").velocity({ opacity: 0 });
  $(".fitimg").velocity({ opacity: 0 });
  $("#features").velocity({ opacity: 0 });
  $("#faq").velocity({ opacity: 0 });
  $("#showcase").velocity({ opacity: 0 });
  $(".b").velocity({ opacity: 0 });
;


  $("#faq").waypoint(function(direction) {
    if (direction === 'up') {
      $(".navbar .navbar-brand").velocity({
        color: "#666"
      }, { duration: "5" });
    }
  }, {
    offset: '2%'
  });



  $("#showcase").waypoint(function() {
    $("#showcase").velocity("fadeIn",
    {duration: 2000 });
    this.destroy()

  }, { offset: '70%'});

  $("#features").waypoint(function() {
    $("#features").velocity("fadeIn",
    {duration: 2000 });
    this.destroy()

  }, { offset: '70%'});





  $("#tagline").velocity("callout.pulse",
  {delay:2500, duration: 1500 });

  $("#mc_embed_signup").velocity("callout.swing",
  {delay: 5000, duration: 700 });

  $(".b").waypoint(function() {
    $(".b").velocity("transition.slideLeftIn",
    {duration: 4000, drag: true });
    this.destroy()

  }, { offset: '60%'});

  $("#fact1").waypoint(function() {
    $("#fact1").velocity("transition.slideLeftIn",
    {duration: 4000, drag: true });
    this.destroy()

  }, { offset: '90%'});

  $("#fact2").waypoint(function() {
    $("#fact2").velocity("transition.slideRightIn",
    {duration: 4000, drag: true });
    this.destroy()

  }, { offset: '90%'});

  $("#about").waypoint(function() {
    $(".info1").velocity("transition.slideRightIn",
    { stagger:400, drag: true });
    this.destroy()
  }, { offset: '50%'});

  $("#features").waypoint(function() {
    $(".fitimg").velocity("transition.slideUpIn",
    { delay:500, duration:2000, stagger:800, drag: true });
    this.destroy()
  }, { offset: '25%'});


});
