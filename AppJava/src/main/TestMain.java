package main;

import gerenciador.Gerenciador;
import protobuff.RequestOuterClass.Response;

public class TestMain {

	public static void main(String[] args) {
		Gerenciador gere = new Gerenciador();
		System.out.println("Alou Mundo!");
		
		gere.estabelecerConexao("localhost", 5205);
		
		gere.enviarRequisicao("1", "0", "0", "0", 0);
		
		Response resposta = gere.receberResposta();
		
		System.out.println("Resposta recebida:");
		
		System.out.println(resposta.getTipoDaMsg());
		System.out.println(resposta.getConteudo());
		
		//while (true);
	}
}
