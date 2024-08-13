package grafo;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
public class Grafo {

	public static void main (String[] args) {
		Nodo cabeza = new Nodo(20);
		Nodo rama1 = new Nodo(19);
		Nodo rama2 = new Nodo(67);
		Nodo hoja1 = new Nodo(99);
		Nodo rama3 = new Nodo(23);
		Nodo hoja2 = new Nodo(57);
		
		cabeza.AsignaValoCentral(rama1);
		cabeza.AsignaValoDerecho(rama3);
		rama1.AsignaValoIzquierdo(rama2);
		rama2.AsignaValoCentral(hoja1);
		rama3.AsignaValoCentral(hoja2);
		Queue<Integer> cola = new LinkedList<>();
		 int ValorEncontrar=57;
		 boolean seguir = true;
		 while(seguir){
			 
		 
		Scanner teclado = new Scanner(System.in);
		System.out.println("¿Que numero desea encontrar?");
		ValorEncontrar = teclado.nextInt();
		
		 boolean encontrado = cabeza.EncuentraValor(ValorEncontrar, cola);
		 while(!cola.isEmpty()) {
			 System.out.print(cola.poll()+" -> " );
		 }
		if(encontrado) {
			System.out.println("valor no encontrado");
		}
		System.out.println(" ");
		System.out.println( "¿desea continuar? 1=Sí otra tecla no");
		int peticion = teclado.nextInt();
		if (peticion!=1) {
			seguir=false;
		}
	}
		
	}
	
	
	
	
	
		
	

}
