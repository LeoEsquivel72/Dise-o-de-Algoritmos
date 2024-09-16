
use core::num;
use std::io;
use rand::Rng;

fn buscalineal(arreglo: &[i32], numeroBuscado: i32) {
    let mut i=0;
    let mut numero_no_encontrado: bool = true;
    while i<arreglo.len() && numero_no_encontrado  {

        if arreglo[i]== numeroBuscado {

            numero_no_encontrado=false;
            
        }else {
            i+=1; 
        }
        
    
    }
    println!("metodo busqueda lineal");
    if numero_no_encontrado {
        println!("El numero {} no se encuentra en la lista de elementos", numeroBuscado);
    }else {
        println!("El numero {} se encuentra en la posicion {}", numeroBuscado, i);
    }
    println!("numero de pasos{}", i)
}
fn ordenaArreglo(arreglo: &mut[i32], principio:usize, finaal:usize){
    let mut inicio=principio;
    let mut fin=finaal;
    let mut pivote=0;
    let mut no_hubo_intercambio=true;
    let mut aux =0;
    if(inicio!=fin && inicio<fin ){
    while inicio!=fin && inicio<fin {
        no_hubo_intercambio=false;
        while inicio!=fin && no_hubo_intercambio{
            if(arreglo[inicio]>arreglo[fin]){
                aux=arreglo[fin];
                arreglo[fin]=arreglo[inicio];
                arreglo[inicio]=aux;
               
                no_hubo_intercambio=false;
               
            } else {
                fin-=1;
            }
            
            
        }
        no_hubo_intercambio=true;
        while inicio !=fin {
            if(arreglo[fin] < arreglo[inicio]){
                aux=arreglo[fin];
                arreglo[fin]=arreglo[inicio];
                arreglo[inicio]=aux;
                
                no_hubo_intercambio=false;
                
            }
            else {
                inicio+=1;
            }
            
        }
    }
    ordenaArreglo(arreglo, principio, fin-1);
    ordenaArreglo(arreglo, fin+1, finaal)
}
}

fn llenaaleatoreo(arreglo: &mut[i32],  numeromin: i32, numeromax: i32) {
    let mut genera_aleatoreo = rand::thread_rng();
    let mut aux=0;
    for num  in 0..arreglo.len() {
        arreglo[aux]= genera_aleatoreo.gen_range(numeromin..numeromax);
        aux+=1;
    }
}

fn busquedabinaria(arreglo: &mut[i32], numeroBuscado: i32){
    let mut i =0;
    let mut numero_no_encontrado = true;
    let mut inicio=0;
    let mut fin=arreglo.len();
    let mut aux =0;

    while numero_no_encontrado && inicio<fin-1 {
        aux=(fin+inicio)/2;
        if arreglo[aux]==numeroBuscado {
            numero_no_encontrado=false;
            
        }else if arreglo[aux]>numeroBuscado {
            fin=aux;
            
        }else {
            inicio=aux;
        }
        i+=1;

    }
    println!("metodo busqueda binaria");
    if numero_no_encontrado{
        println!("el numero  {}  no se encuentra en el arreglo", numeroBuscado);
    }else {
        println!("el numero  {} se encuentra en la posicion  {} ", numeroBuscado, aux);
    }
    println!("numero de pasos  {}", i);




}
fn busquedacentinela(arreglo: &mut[i32], numeroBuscado: i32){
    let mut aux=arreglo[arreglo.len()-1];
    arreglo[arreglo.len()-1]= numeroBuscado;
    let mut i=0;
    while numeroBuscado!=arreglo[i] {
        i+=1;
        
    }
    arreglo[arreglo.len()-1]=aux;
    println!("metodo busqueda con centinela");
    if(numeroBuscado== aux|| i<arreglo.len()-1){
        
        println!("El numero {} se encuentra en la posicion {}", numeroBuscado, i);

    }else {
        println!("El numero{} no se encuentra en el arreglo", numeroBuscado);
        
    }
    println!("numero de pasos{}", i);
}

fn main() {
  
    let mut numeroBuscado = 25;
    
    let mut valor_minimo:i32=0;
    let mut valor_maximo:i32=0;
    println!("De que tamaño quieres el arreglo");
    let mut entrada= String::new();
    let mut numero:String = String::new();
    io:: stdin().read_line(& mut entrada);
    
    let lectura : usize = entrada.trim().parse().expect("necesito un entero");
    let tamanio: usize = lectura;
    let mut arreglo=vec![0;tamanio];

    println!("¿en qué rango de valores quieres quieres llenar el arreglo?");
    println!("rango inferior: ");
    io::stdin().read_line( &mut numero);
    valor_minimo = numero.trim().parse().expect("necesito un entero");

    println!("rango superior: ");
    numero=String ::new();
    io::stdin().read_line( &mut numero);
    valor_maximo=numero.trim().parse().expect("necesito un entero");

    println!("numero a encontrar: ");
    numero=String ::new();
    io::stdin().read_line( &mut numero);
    numeroBuscado=numero.trim().parse().expect("necesito un entero");

    llenaaleatoreo(&mut arreglo, valor_minimo,valor_maximo);
    println!("el arreglo antes de ordenar {:?}", arreglo);

    println!("\n ejecución antes de ordenar \n");

    busquedabinaria(&mut arreglo, numeroBuscado);
    buscalineal(&mut arreglo, numeroBuscado);
    busquedacentinela(&mut arreglo, numeroBuscado);
    
    let mut finaal=arreglo.len()-1;
    ordenaArreglo(&mut arreglo, 0, finaal);

    println!("\n el arreglo despues de ordenar \n {:?}", arreglo);
    println!("\n despues de ordenar el arreglo \n");
    busquedabinaria(&mut arreglo, numeroBuscado);
    buscalineal(&mut arreglo, numeroBuscado);
    busquedacentinela(&mut arreglo, numeroBuscado);
    
   
}
