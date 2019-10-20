package main;

import gerenciador.Gerenciador;
import protobuff.RequestOuterClass.*;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		Gerenciador gere = new Gerenciador();
		gere.estabelecerConexao("localhost", 5205);
		
		String opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:close";
		
		while (true) {
			System.out.print("\n==============================\n\n" + opcoes + "\n\nR: ");
			int opc = in.nextInt();
			in.nextLine();
			
			if (opc == 1) {
				gere.enviarRequisicao("1", "1", "", "", 0);
			} else if (opc == 2) {
				System.out.print("\nDigite o nome do dispositivo: ");
				String nomeDisp = in.nextLine();
				
				gere.enviarRequisicao("2", "2", nomeDisp, "", 0);
			} else if (opc == 3) {
				System.out.print("\nDigite o nome do dispositivo: ");
				String nomeDisp = in.nextLine();
				
				System.out.print("Digite o número da função: ");
				String nomeFunc = in.nextLine();
				
				System.out.print("Digite um valor se a função for set: ");
				int valor = in.nextInt();
				
				gere.enviarRequisicao("3", "2", nomeDisp, nomeFunc, valor);
			} else if (opc == 4) {
				gere.enviarRequisicao("4", "1", "", "", 0);
			} else if (opc == 5) {
				gere.enviarRequisicao("close", "", "", "", 0);
			} else {
				System.out.println("ERRO: Opção escolhida não é válida. Digite uma opção válida!");
			}
			
			Response resposta = gere.receberResposta();
			System.out.println("\n------------------------------\n\nTipo da mensagem: " + resposta.getTipoDaMsg());
			System.out.println("Conteúdo da mensagem: " + resposta.getConteudo());
		}
	}
}
