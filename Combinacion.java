package Algoritmo;
import java.util.Scanner;

public class Combinacion {
/* La complejidad temporal del algoritmo es cuadrática ya que recorre n veces n elementos
 * además el contador así lo demuestra */
	public static void main (String[] args ) {
		Scanner teclado = new Scanner(System.in);
		System.out.println("Hasta que numero deseas hacer intercambios");
		int valor = teclado.nextInt();
		int contador=0;
		for (int i=0;i<valor; i++ ) {
			for(int j=0; j<valor; j++) {
				System.out.println(i+1 + ","+(j+1));
				contador++;
			}
		}
		System.out.println("numero de pasos " + contador);
	}
}
