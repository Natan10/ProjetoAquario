package gerenciador;

import java.net.*;
import java.io.*;
import protobuff.RequestOuterClass.*;

public class Gerenciador {
	private Socket s;
	private DataOutputStream saida;
	private DataInputStream entrada;
	
	public Gerenciador() {
		s = null;
		saida = null;
		entrada = null;
	}
	
	public void estabelecerConexao(String serverIP, int serverPort) {
		try {
			s = new Socket(serverIP, serverPort);
			saida = new DataOutputStream(s.getOutputStream());
			entrada = new DataInputStream(s.getInputStream());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public void encerrarConexao() {
		try {
			s.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public void enviarRequisicao(String comando, String tipo, String nomeDisp, String nomeFunc, int valor) {
		try {
			Request.Builder req = Request.newBuilder();
			req.setComando(comando);
			req.setTipoDaMsg(tipo);
			req.setNomeDoDisp(nomeDisp);
			req.setNomeDaFunc(nomeFunc);
			req.setValor(valor);
			
			req.build().writeTo(saida);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	//reatUTF com problma de travar
	public Response receberResposta() {
		try {
			Thread.sleep(1000);
			
			int a = entrada.available();
			byte b[] = new byte[a];
			
			entrada.read(b);
			
			return Response.parseFrom(b);
		} catch (IOException | InterruptedException e) {
			e.printStackTrace();
		}
		
		return null;
	}
}
