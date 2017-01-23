

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
  $("#tagline").velocity({ opacity: 0 });
  $("#fact1").velocity({ opacity: 0 });
  $("#fact2").velocity({ opacity: 0 });
  $(".fitimg").velocity({ opacity: 0 });


  $(".cta").waypoint(function(direction) {
    if (direction === 'down') {
      $(".navbar .navbar-brand").velocity({
        color: "#FFFFFF"
      }, { duration: "5" });
    }
  }, {
    offset: '2%'
  });


  $(".cta").waypoint(function(direction) {
    if (direction === 'up') {
      $(".navbar .navbar-brand").velocity({
        color: "#F64747"
      }, { duration: "5" });
    }
  }, {
    offset: '1%'
  });

  $("#about").waypoint(function(direction) {
    if (direction === 'up') {
      $(".navbar .navbar-brand").velocity({
        color: "#FFFFFF"
      }, { duration: "5" });
    }
  }, {
    offset: '1%'
  });

  $("#about").waypoint(function(direction) {
    if (direction === 'down') {
      $(".navbar .navbar-brand").velocity({
        color: "#F64747"
      }, { duration: "5" });
    }
  }, {
    offset: '1%'
  });

  $("#work").waypoint(function(direction) {
    if (direction === 'up') {
      $(".navbar .navbar-brand").velocity({
        color: "#FFFFFF"
      }, { duration: "5" });
    }
  }, {
    offset: '1%'
  });

  $("#work").waypoint(function(direction) {
    if (direction === 'down') {
      $(".navbar .navbar-brand").velocity({
        color: "#F64747"
      }, { duration: "5" });
    }
  }, {
    offset: '1%'
  });

  $("#home").waypoint(function(direction) {
    if (direction === 'up') {
      $(".navbar .navbar-brand").velocity({
        color: "#F64747"
      }, { duration: "5" });
    }
  }, {
    offset: '75%'
  });

  $("#tagline").velocity("fadeIn",
  {delay: 300, duration: 2500 });

  $("#tagline").velocity("callout.pulse",
  {duration: 1500 });

  $("#mc_embed_signup").velocity("callout.swing",
  {delay: 5000, duration: 700 });


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
    { duration:2000, stagger:800, drag: true });
    this.destroy()
  }, { offset: '25%'});


});
