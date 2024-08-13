package grafo;

import java.util.Queue;
import java.util.LinkedList;
public class Nodo {
	int valor;
	Nodo izquierdo;
	Nodo central;
	Nodo derecho;

	
	Nodo(int Valor){
		valor=Valor;
		central = null;
		izquierdo=null;
		derecho=null;
	}
	public void AsignaValoIzquierdo(Nodo NuevoNodo){
		izquierdo= NuevoNodo;
		
	}
	public void AsignaValoDerecho(Nodo NuevoNodo){
		derecho = NuevoNodo;
		
	}
	public void AsignaValoCentral(Nodo NuevoNodo){
		central= NuevoNodo;
		
	}
	public boolean EncuentraValor(int ValorPorEncontrar, Queue<Integer> Cola) {
		boolean ValorNoEncontrado = true;


		
		Cola.add(valor);
		if(valor==ValorPorEncontrar) {
			ValorNoEncontrado=false;
		}
		
		 if((izquierdo != null )&& ValorNoEncontrado) {
			ValorNoEncontrado= izquierdo.EncuentraValor(ValorPorEncontrar, Cola);
		}
		if((central != null )&& ValorNoEncontrado) {
			ValorNoEncontrado = central.EncuentraValor(ValorPorEncontrar, Cola);
		}
		if((derecho != null )&& ValorNoEncontrado) {
			ValorNoEncontrado = derecho.EncuentraValor(ValorPorEncontrar, Cola);
		}
		
		return ValorNoEncontrado;
		}
	
}
