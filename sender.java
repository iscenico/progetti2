package screeenshare;

import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.Listener;
import org.bukkit.plugin.java.JavaPlugin;

public class sender extends JavaPlugin implements Listener{
	
	public void onEnable() {
		getServer().getMessenger().registerOutgoingPluginChannel(this, "Bungeecord");
	}
	
	public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
		if(label.equalsIgnoreCase("teleport")) {
			sendToServer(((Player)sender), args[0]);
		}
		return false;
	}
	
	public void sendToServer(Player player, String targetserver) {
		ByteArrayOutputStream b = new ByteArrayOutputStream();
		DataOutputStream out = new DataOutputStream(b);
		try {
			out.writeUTF("Connect");
			out.writeUTF(targetserver);
		}catch (Exception e) {
			e.printStackTrace();
		}
		player.sendPluginMessage(this, "Bungeecord", b.toByteArray());
	}
}
