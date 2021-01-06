Query.datetimepicker.setLocale('de');

jQuery('#datetimepicker1').datetimepicker({
 i18n:{
  de:{
   months:[
    'Januar','Februar','März','April',
    'Mai','Juni','Juli','August',
    'September','Oktober','November','Dezember',
   ],
   dayOfWeek:[
    "So.", "Mo", "Di", "Mi", 
    "Do", "Fr", "Sa.",
   ]
  }
 },
 timepicker:false,
 format:'d.m.Y'
});


jQuery('#datetimepicker2').datetimepicker({
  datepicker:false,
  format:'H:i'
});


jQuery('#datetimepicker_start_time').datetimepicker({
  startDate:'+1971/05/01'//or 1986/12/08
});


jQuery('#datetimepicker_unixtime').datetimepicker({
  format:'unixtime'
});


jQuery('#datetimepicker3').datetimepicker({
  format:'d.m.Y H:i',
  inline:true,
  lang:'ru'
});