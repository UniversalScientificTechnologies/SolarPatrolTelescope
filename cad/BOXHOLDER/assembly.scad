$fn=60;

polomer=38;
sirka_drzaku=8;
sila_drzaku=4;

prumer_sroubu=3.2;
vyska_matky=3;
sirka_matky=6.7;
presah_pro_drzak_sroubu=10;
mezera_mezi_dilci=3;

 translate([0,0,sirka_drzaku/2]) 
drzak_1();

module drzak_1(){


//ovál
difference () {
       
    union()   {  
        
    //drzak    
    cube([2*polomer+2*sila_drzaku+2*presah_pro_drzak_sroubu,2*sila_drzaku+mezera_mezi_dilci,sirka_drzaku],true);    
   
        
    //drzak u boxu    
    translate([0,polomer+sila_drzaku/2,0]) 
      cube([2*polomer+2*sila_drzaku+2*presah_pro_drzak_sroubu,sila_drzaku,sirka_drzaku],true);
    
    //kruh
    cylinder(h=sirka_drzaku, r=polomer+sila_drzaku, center=true);   
       
    //bocni vystuhy   
      translate([polomer+sila_drzaku+presah_pro_drzak_sroubu/2-3/2,polomer/2,0]) 
      cube([presah_pro_drzak_sroubu+3,polomer,sirka_drzaku],true);  
        
        
           translate([-polomer-sila_drzaku-presah_pro_drzak_sroubu/2+3/2,polomer/2,0]) 
      cube([presah_pro_drzak_sroubu+3,polomer,sirka_drzaku],true); 



        
} 
    cylinder(h=sirka_drzaku, r=polomer, center=true); 

    //mezera mezi dilci
cube([2*polomer+2*sila_drzaku+2*presah_pro_drzak_sroubu,mezera_mezi_dilci,sirka_drzaku],true);  


//otvor na sroub
rotate([90, 0, 0])
translate([polomer+sila_drzaku+presah_pro_drzak_sroubu/2,0,0]) 
cylinder(h=2*polomer+2*sila_drzaku+mezera_mezi_dilci, r=prumer_sroubu/2, center=true); 

rotate([90, 0, 0])
translate([-polomer-sila_drzaku-presah_pro_drzak_sroubu/2,0,0]) 
cylinder(h=2*polomer+2*sila_drzaku+mezera_mezi_dilci, r=prumer_sroubu/2, center=true); 


//otvor na matku
    translate([polomer+sila_drzaku+presah_pro_drzak_sroubu/2,mezera_mezi_dilci/2,0]) 
    rotate([-90, 0, 0])
    cylinder (h = vyska_matky+0.31, r= (sirka_matky+0.2)/2, $fn=6); 

translate([-polomer-sila_drzaku-presah_pro_drzak_sroubu/2,mezera_mezi_dilci/2,0]) 
    rotate([-90, 0, 0])
    cylinder (h = vyska_matky+0.31, r= (sirka_matky+0.2)/2, $fn=6); 



} 

 
   
    } 

      
  
 