package com.ads.caching.entity;

import java.io.Serializable;

import org.springframework.data.annotation.Id;
import org.springframework.data.redis.core.RedisHash;



@RedisHash
public class NASAData  implements Serializable{
	
	public NASAData(String id, String visualize, String timestamp) {
		super();
		this.id = id;
		this.visualize = visualize;
		this.timestamp = timestamp;
	}
	
	public NASAData() {};
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getVisualize() {
		return visualize;
	}
	public void setVisualize(String visualize) {
		this.visualize = visualize;
	}
	public String getTimestamp() {
		return timestamp;
	}
	public void setTimestamp(String timestamp) {
		this.timestamp = timestamp;
	}
	@Id
	private String id;
	private String visualize;
	private String timestamp;
	

}
