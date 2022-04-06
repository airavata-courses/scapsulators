package com.ads.caching.config;

import java.util.HashMap;
import java.util.Map;

import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.common.serialization.ByteArrayDeserializer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.kafka.annotation.EnableKafka;
import org.springframework.kafka.config.ConcurrentKafkaListenerContainerFactory;
import org.springframework.kafka.core.ConsumerFactory;
import org.springframework.kafka.core.DefaultKafkaConsumerFactory;
import org.springframework.kafka.support.serializer.JsonDeserializer;

import com.ads.caching.entity.NASAData;

@EnableKafka
@Configuration
public class ConsumerConfiguration {
	@Bean
    public ConsumerFactory<String, byte[]>   studentConsumer()
    {
 
		//JsonDeserializer<NASAData> deserializer = new JsonDeserializer<>(NASAData.class);
        //deserializer.addTrustedPackages("*");
		//org.springframework.kafka.support.converter.ByteArrayJsonMessageConverter
		
		

        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka:9092,localhost:9093");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "caching_NASA");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, ByteArrayDeserializer.class);
        return new DefaultKafkaConsumerFactory<>(props, new StringDeserializer(), new ByteArrayDeserializer());
    }
 
    @Bean
    public ConcurrentKafkaListenerContainerFactory<String,byte[]> studentListner()
    {
        ConcurrentKafkaListenerContainerFactory<String,byte[]>
            factory  = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(studentConsumer());
        return factory;
    }

}
