# Dictionary Format: (tanbeta, collider) : (runCode, sinbma, xsec, xsecunc) )

# sin(beta-alpha) = +1
bma_bb = { 
    ('1' , 'cepc'):('01','1','4.138e-05','2.0e-07'), 
    ('2' , 'cepc'):('02','1','4.160e-05','2.1e-07'),
    ('3' , 'cepc'):('03','1','4.138e-05','2.0e-07'), 
    ('4' , 'cepc'):('04','1','4.160e-05','2.3e-07'),
    ('5' , 'cepc'):('05','1','4.168e-05','2.4e-07'),
    ('6' , 'cepc'):('06','1','4.149e-05','1.9e-07'),
    ('7' , 'cepc'):('07','1','4.164e-05','2.6e-07'),
    ('8' , 'cepc'):('08','1','4.152e-05','1.9e-07'),
    ('9' , 'cepc'):('09','1','4.153e-05','2.0e-07'), 
    ('10', 'cepc'):('10','1','4.136e-05','2.4e-07'),
    ('12', 'cepc'):('11','1','4.145e-05','1.9e-07'),
    ('14', 'cepc'):('12','1','4.145e-05','2.0e-07'), 
    ('16', 'cepc'):('13','1','4.177e-05','1.9e-07'),
    ('18', 'cepc'):('14','1','4.129e-05','2.1e-07'),
    ('20', 'cepc'):('15','1','4.121e-05','2.0e-07'), 
    ('22', 'cepc'):('16','1','4.137e-05','2.0e-07'), 
    ('24', 'cepc'):('17','1','4.136e-05','1.9e-07'),
    ('26', 'cepc'):('18','1','4.141e-05','1.8e-07'),
    ('28', 'cepc'):('19','1','4.136e-05','2.2e-07'),
    ('30', 'cepc'):('20','1','4.102e-05','2.3e-07'),
    ('32', 'cepc'):('21','1','4.152e-05','1.9e-07'),
    ('34', 'cepc'):('22','1','4.171e-05','1.9e-07'),
    ('36', 'cepc'):('23','1','4.133e-05','2.2e-07'),
    ('38', 'cepc'):('24','1','4.123e-05','2.1e-07'),
    ('40', 'cepc'):('25','1','4.196e-05','2.4e-07'),
    ('42', 'cepc'):('26','1','4.186e-05','2.0e-07'), 
    ('44', 'cepc'):('27','1','4.157e-05','1.1e-07'),
    ('46', 'cepc'):('28','1','4.146e-05','1.9e-07'),
    ('48', 'cepc'):('29','1','4.133e-05','1.9e-07'),
    ('50', 'cepc'):('30','1','4.146e-05','1.8e-07'),
    ('1' , 'ilc'):('01','1','9.242e-06','5.1e-08'),
    ('2' , 'ilc'):('02','1','9.175e-06','6.7e-08'),
    ('3' , 'ilc'):('03','1','9.188e-06','2.9e-08'),
    ('4' , 'ilc'):('04','1','9.201e-06','4.1e-08'),
    ('5' , 'ilc'):('05','1','9.092e-06','5.0e-08'),  
    ('6' , 'ilc'):('06','1','9.279e-06','4.9e-08'),
    ('7' , 'ilc'):('07','1','9.177e-06','4.9e-08'),
    ('8' , 'ilc'):('08','1','9.138e-06','3.5e-08'),
    ('9' , 'ilc'):('09','1','9.207e-06','4.8e-08'),
    ('10', 'ilc'):('10','1','9.203e-06','5.9e-08'),
    ('12', 'ilc'):('11','1','9.137e-06','2.9e-08'),
    ('14', 'ilc'):('12','1','9.261e-06','5.4e-08'),
    ('16', 'ilc'):('13','1','9.274e-06','4.1e-08'),
    ('18', 'ilc'):('14','1','9.143e-06','5.0e-08'),  
    ('20', 'ilc'):('15','1','9.244e-06','2.9e-08'),
    ('22', 'ilc'):('16','1','9.163e-06','4.9e-08'),
    ('24', 'ilc'):('17','1','9.187e-06','5.4e-08'),
    ('26', 'ilc'):('18','1','9.253e-06','4.9e-08'),
    ('28', 'ilc'):('19','1','9.137e-06','4.1e-08'),
    ('30', 'ilc'):('20','1','9.098e-06','4.9e-08'),
    ('32', 'ilc'):('21','1','9.221e-06','4.9e-08'),
    ('34', 'ilc'):('22','1','9.298e-06','4.9e-08'),
    ('36', 'ilc'):('23','1','9.173e-06','5.2e-08'),
    ('38', 'ilc'):('24','1','9.157e-06','4.8e-08'),
    ('40', 'ilc'):('25','1','9.221e-06','3.3e-08'),
    ('42', 'ilc'):('26','1','9.229e-06','4.1e-08'),
    ('44', 'ilc'):('27','1','9.197e-06','5.0e-08'),  
    ('46', 'ilc'):('28','1','9.208e-06','4.2e-08'),
    ('48', 'ilc'):('29','1','9.190e-06','6.9e-08'), 
    ('50', 'ilc'):('30','1','9.160e-06','5.5e-08')  
}

# sin(beta+alpha) = +1  ---------> sin(beta-alpha) = (tanbeta^2 - 1)/( tanbeta^2 + 1)
bpa_bb = { 
    ('2' , 'cepc'):('31','0.6'     ,'1.491e-05','7.1e-08'),
    ('3' , 'cepc'):('32','0.8'     ,'2.638e-05','1.2e-07'),
    ('4' , 'cepc'):('33','0.882353','3.245e-05','1.3e-07'),
    ('5' , 'cepc'):('34','0.923077','3.523e-05','1.6e-07'),
    ('6' , 'cepc'):('35','0.945946','3.697e-05','1.4e-07'),
    ('7' , 'cepc'):('36','0.96'    ,'3.800e-05','2.9e-07'), 
    ('8' , 'cepc'):('37','0.969231','3.869e-05','2.0e-07'), 
    ('9' , 'cepc'):('38','0.97561' ,'3.950e-05','1.8e-07'),
    ('10', 'cepc'):('39','0.980198','3.954e-05','2.4e-07'),
    ('12', 'cepc'):('40','0.986207','4.013e-05','1.9e-07'),
    ('14', 'cepc'):('41','0.989848','4.058e-05','1.1e-07'),
    ('16', 'cepc'):('42','0.992218','4.079e-05','2.0e-07'), 
    ('18', 'cepc'):('43','0.993846','4.107e-05','1.9e-07'),
    ('20', 'cepc'):('44','0.995012','4.067e-05','2.2e-07'),
    ('22', 'cepc'):('45','0.995876','4.103e-05','2.1e-07'),
    ('24', 'cepc'):('46','0.996534','4.135e-05','2.9e-07'),
    ('26', 'cepc'):('47','0.997046','4.097e-05','1.9e-07'),
    ('28', 'cepc'):('48','0.997452','4.149e-05','2.9e-07'),
    ('30', 'cepc'):('49','0.99778' ,'4.093e-05','2.6e-07'),
    ('32', 'cepc'):('50','0.998049','4.122e-05','1.9e-07'),
    ('34', 'cepc'):('51','0.998271','4.107e-05','1.9e-07'),
    ('36', 'cepc'):('52','0.998458','4.123e-05','1.9e-07'),
    ('38', 'cepc'):('53','0.998616','4.088e-05','2.1e-07'),
    ('40', 'cepc'):('54','0.998751','4.119e-05','2.4e-07'),
    ('42', 'cepc'):('55','0.998867','4.137e-05','1.9e-07'),
    ('44', 'cepc'):('56','0.998967','4.144e-05','2.0e-07'), 
    ('46', 'cepc'):('57','0.999055','4.150e-05','2.0e-07'),  
    ('48', 'cepc'):('58','0.999132','4.116e-05','1.9e-07'),
    ('50', 'cepc'):('59','0.9992'  ,'4.137e-05','2.0e-07'), 
    ('2' , 'ilc'):('31','0.6'     ,'3.308e-06','1.8e-08'),
    ('3' , 'ilc'):('32','0.8'     ,'5.874e-06','5.5e-08'),
    ('4' , 'ilc'):('33','0.882353','7.103e-06','4.0e-08'),  
    ('5' , 'ilc'):('34','0.923077','7.820e-06','2.5e-08'), 
    ('6' , 'ilc'):('35','0.945946','8.207e-06','4.5e-08'),
    ('7' , 'ilc'):('36','0.96'    ,'8.484e-06','4.9e-08'),
    ('8' , 'ilc'):('37','0.969231','8.559e-06','4.8e-08'),
    ('9' , 'ilc'):('38','0.97561' ,'8.820e-06','2.8e-08'), 
    ('10', 'ilc'):('39','0.980198','8.774e-06','4.6e-08'),
    ('12', 'ilc'):('40','0.986207','8.924e-06','5.4e-08'),
    ('14', 'ilc'):('41','0.989848','9.057e-06','2.9e-08'),
    ('16', 'ilc'):('42','0.992218','9.015e-06','5.6e-08'),
    ('18', 'ilc'):('43','0.993846','9.132e-06','3.5e-08'),
    ('20', 'ilc'):('44','0.995012','9.095e-06','5.2e-08'),
    ('22', 'ilc'):('45','0.995876','9.064e-06','5.2e-08'),
    ('24', 'ilc'):('46','0.996534','9.145e-06','6.8e-08'),
    ('26', 'ilc'):('47','0.997046','9.143e-06','3.0e-08'),  
    ('28', 'ilc'):('48','0.997452','9.184e-06','4.0e-08'),  
    ('30', 'ilc'):('49','0.99778' ,'9.070e-06','7.5e-08'), 
    ('32', 'ilc'):('50','0.998049','9.168e-06','4.9e-08'),
    ('34', 'ilc'):('51','0.998271','9.112e-06','4.9e-08'),
    ('36', 'ilc'):('52','0.998458','9.144e-06','2.9e-08'),
    ('38', 'ilc'):('53','0.998616','9.115e-06','5.8e-08'),
    ('40', 'ilc'):('54','0.998751','9.101e-06','5.6e-08'),
    ('42', 'ilc'):('55','0.998867','9.175e-06','5.0e-08'),  
    ('44', 'ilc'):('56','0.998967','9.232e-06','4.7e-08'),
    ('46', 'ilc'):('57','0.999055','9.235e-06','4.0e-08'),  
    ('48', 'ilc'):('58','0.999132','9.108e-06','4.9e-08'),
    ('50', 'ilc'):('59','0.9992'  ,'9.226e-06','5.5e-08') 
}

# sin(beta-alpha) = +1
bma_mumu = { 
    ('1' , 'cepc'):('01','1','9.200e-06','4.1e-08'),  
    ('2' , 'cepc'):('02','1','9.182e-06','4.5e-08'),
    ('3' , 'cepc'):('03','1','9.203e-06','4.9e-08'),
    ('4' , 'cepc'):('04','1','9.148e-06','5.4e-08'),
    ('5' , 'cepc'):('05','1','9.251e-06','4.1e-08'),
    ('6' , 'cepc'):('06','1','9.196e-06','4.9e-08'),
    ('7' , 'cepc'):('07','1','9.134e-06','4.9e-08'),
    ('8' , 'cepc'):('08','1','9.337e-06','5.0e-08'),  
    ('9' , 'cepc'):('09','1','9.209e-06','6.8e-08'),
    ('10', 'cepc'):('10','1','9.194e-06','4.9e-08'),
    ('12', 'cepc'):('11','1','9.059e-06','8.0e-08'),  
    ('14', 'cepc'):('12','1','9.196e-06','5.0e-08'),  
    ('16', 'cepc'):('13','1','9.187e-06','5.0e-08'),  
    ('18', 'cepc'):('14','1','9.184e-06','4.8e-08'),
    ('20', 'cepc'):('15','1','9.163e-06','2.9e-08'),
    ('22', 'cepc'):('16','1','9.149e-06','7.2e-08'),
    ('24', 'cepc'):('17','1','9.190e-06','3.0e-08'),   
    ('26', 'cepc'):('18','1','9.217e-06','9.5e-08'),
    ('28', 'cepc'):('19','1','9.211e-06','5.3e-08'),
    ('30', 'cepc'):('20','1','9.222e-06','4.9e-08'),
    ('32', 'cepc'):('21','1','9.249e-06','5.7e-08'),
    ('34', 'cepc'):('22','1','9.155e-06','5.2e-08'),
    ('36', 'cepc'):('23','1','9.130e-06','5.4e-08'), 
    ('38', 'cepc'):('24','1','9.267e-06','5.0e-08'),  
    ('40', 'cepc'):('25','1','9.247e-06','6.0e-08'),  
    ('42', 'cepc'):('26','1','9.275e-06','4.9e-08'),
    ('44', 'cepc'):('27','1','9.129e-06','6.6e-08'),
    ('46', 'cepc'):('28','1','9.200e-06','5.0e-08'),    
    ('48', 'cepc'):('29','1','9.115e-06','5.0e-08'),  
    ('50', 'cepc'):('30','1','9.175e-06','4.9e-08'),
    ('1' , 'ilc'):('01','1','1.591e-06','9.8e-09'),
    ('2' , 'ilc'):('02','1','1.595e-06','1.1e-08'),
    ('3' , 'ilc'):('03','1','1.585e-06','1.1e-08'),
    ('4' , 'ilc'):('04','1','1.581e-06','1.2e-08'),
    ('5' , 'ilc'):('05','1','1.604e-06','8.9e-09'),
    ('6' , 'ilc'):('06','1','1.598e-06','1.1e-08'),
    ('7' , 'ilc'):('07','1','1.586e-06','1.2e-08'),
    ('8' , 'ilc'):('08','1','1.596e-06','1.2e-08'),
    ('9' , 'ilc'):('09','1','1.582e-06','9.9e-09'),
    ('10', 'ilc'):('10','1','1.616e-06','1.2e-08'),
    ('12', 'ilc'):('11','1','1.607e-06','9.9e-09'),
    ('14', 'ilc'):('12','1','1.590e-06','1.4e-08'), 
    ('16', 'ilc'):('13','1','1.594e-06','9.8e-09'),
    ('18', 'ilc'):('14','1','1.586e-06','1.2e-08'),
    ('20', 'ilc'):('15','1','1.601e-06','7.6e-09'),
    ('22', 'ilc'):('16','1','1.603e-06','1.3e-08'),
    ('24', 'ilc'):('17','1','1.596e-06','1.2e-08'),
    ('26', 'ilc'):('18','1','1.597e-06','7.6e-09'),
    ('28', 'ilc'):('19','1','1.601e-06','7.6e-09'),
    ('30', 'ilc'):('20','1','1.588e-06','1.2e-08'),
    ('32', 'ilc'):('21','1','1.600e-06','1.2e-08'),  
    ('34', 'ilc'):('22','1','1.605e-06','9.7e-09'),
    ('36', 'ilc'):('23','1','1.580e-06','1.1e-08'), 
    ('38', 'ilc'):('24','1','1.598e-06','1.2e-08'),
    ('40', 'ilc'):('25','1','1.587e-06','1.2e-08'),
    ('42', 'ilc'):('26','1','1.598e-06','1.4e-08'),
    ('44', 'ilc'):('27','1','1.585e-06','1.2e-08'),
    ('46', 'ilc'):('28','1','1.577e-06','9.8e-09'),
    ('48', 'ilc'):('29','1','1.606e-06','1.5e-08'),
    ('50', 'ilc'):('30','1','1.603e-06','1.2e-08') 
}

# sin(beta+alpha) = +1  ---------> sin(beta-alpha) = (tanbeta^2 - 1)/( tanbeta^2 + 1)
bpa_mumu = { 
    ('2' , 'cepc'):('31','0.6'     ,'3.311e-06','9.5e-09'),
    ('3' , 'cepc'):('32','0.8'     ,'5.863e-06','3.1e-08'),
    ('4' , 'cepc'):('33','0.882353','7.181e-06','3.8e-08'),
    ('5' , 'cepc'):('34','0.923077','7.871e-06','4.6e-08'),
    ('6' , 'cepc'):('35','0.945946','8.267e-06','3.8e-08'),
    ('7' , 'cepc'):('36','0.96'    ,'8.408e-06','6.3e-08'),
    ('8' , 'cepc'):('37','0.969231','8.677e-06','4.5e-08'),
    ('9' , 'cepc'):('38','0.97561' ,'8.775e-06','5.5e-08'),
    ('10', 'cepc'):('39','0.980198','8.865e-06','2.8e-08'),
    ('12', 'cepc'):('40','0.986207','8.911e-06','2.9e-08'),
    ('14', 'cepc'):('41','0.989848','8.950e-06','7.0e-08'),   
    ('16', 'cepc'):('42','0.992218','9.057e-06','4.9e-08'),
    ('18', 'cepc'):('43','0.993846','9.129e-06','5.3e-08'),
    ('20', 'cepc'):('44','0.995012','9.072e-06','1.0e-07'),  
    ('22', 'cepc'):('45','0.995876','9.203e-06','4.2e-08'),
    ('24', 'cepc'):('46','0.996534','9.186e-06','5.9e-08'),
    ('26', 'cepc'):('47','0.997046','9.154e-06','4.9e-08'),
    ('28', 'cepc'):('48','0.997452','9.125e-06','5.6e-08'),
    ('30', 'cepc'):('49','0.99778' ,'9.123e-06','4.8e-08'),
    ('32', 'cepc'):('50','0.998049','9.164e-06','4.1e-08'),
    ('34', 'cepc'):('51','0.998271','9.177e-06','5.0e-08'),  
    ('36', 'cepc'):('52','0.998458','9.217e-06','7.6e-08'),
    ('38', 'cepc'):('53','0.998616','9.132e-06','5.2e-08'),
    ('40', 'cepc'):('54','0.998751','9.091e-06','4.9e-08'),
    ('42', 'cepc'):('55','0.998867','9.161e-06','3.0e-08'),  
    ('44', 'cepc'):('56','0.998967','9.213e-06','5.1e-08'),
    ('46', 'cepc'):('57','0.999055','9.155e-06','4.9e-08'),
    ('48', 'cepc'):('58','0.999132','9.167e-06','3.3e-08'),
    ('50', 'cepc'):('59','0.9992'  ,'9.186e-06','3.3e-08'),
    ('2' , 'ilc'):('31','0.6'     ,'5.718e-07','4.3e-09'),
    ('3' , 'ilc'):('32','0.8'     ,'1.021e-06','6.3e-09'),
    ('4' , 'ilc'):('33','0.882353','1.249e-06','1.1e-08'),
    ('5' , 'ilc'):('34','0.923077','1.373e-06','8.5e-09'),
    ('6' , 'ilc'):('35','0.945946','1.421e-06','8.8e-09'),
    ('7' , 'ilc'):('36','0.96'    ,'1.466e-06','1.1e-08'),
    ('8' , 'ilc'):('37','0.969231','1.495e-06','9.0e-09'),  
    ('9' , 'ilc'):('38','0.97561' ,'1.539e-06','9.5e-09'),
    ('10', 'ilc'):('39','0.980198','1.523e-06','1.2e-08'),
    ('12', 'ilc'):('40','0.986207','1.556e-06','1.1e-08'),
    ('14', 'ilc'):('41','0.989848','1.565e-06','7.3e-09'),
    ('16', 'ilc'):('42','0.992218','1.580e-06','9.7e-09'), 
    ('18', 'ilc'):('43','0.993846','1.583e-06','7.6e-09'),
    ('20', 'ilc'):('44','0.995012','1.588e-06','9.7e-09'),
    ('22', 'ilc'):('45','0.995876','1.587e-06','7.4e-09'),
    ('24', 'ilc'):('46','0.996534','1.575e-06','1.2e-08'),
    ('26', 'ilc'):('47','0.997046','1.590e-06','1.4e-08'), 
    ('28', 'ilc'):('48','0.997452','1.591e-06','1.1e-08'),
    ('30', 'ilc'):('49','0.99778' ,'1.593e-06','9.9e-09'),
    ('32', 'ilc'):('50','0.998049','1.603e-06','1.2e-08'),
    ('34', 'ilc'):('51','0.998271','1.585e-06','1.5e-08'),
    ('36', 'ilc'):('52','0.998458','1.601e-06','7.4e-09'),
    ('38', 'ilc'):('53','0.998616','1.590e-06','1.4e-08'), 
    ('40', 'ilc'):('54','0.998751','1.594e-06','1.4e-08'),
    ('42', 'ilc'):('55','0.998867','1.590e-06','1.2e-08'), 
    ('44', 'ilc'):('56','0.998967','1.596e-06','1.1e-08'),
    ('46', 'ilc'):('57','0.999055','1.596e-06','7.5e-09'),
    ('48', 'ilc'):('58','0.999132','1.590e-06','1.4e-08'), 
    ('50', 'ilc'):('59','0.9992'  ,'1.605e-06','1.3e-08') 
}



d1 = { ('bma','ilc',  '{i}'.format(i=i)): ( '01','0.0018030','1.2e-05','0.0815942') for i in range(1,51) }
d2 = { ('bma','cepc', '{i}'.format(i=i)): ( '01','0.008177','5.8e-05','0.0815942')  for i in range(1,51) }

# (scenario, collider, tanbeta) : ( runCode, xsec, xsecUnc, branchingRatio)
gg = { 
    
('bpa', 'ilc','2' ) : ( '02','0.0006564','3.4e-06','0.1199650'),
('bpa', 'ilc','5' ) : ( '03','0.0015390','1.0e-05','0.1051740'),
('bpa', 'ilc','10') : ( '04','0.0017200','9.3e-06','0.1023830'),
('bpa', 'cepc', '2' ) : ( '02','0.002966','2.0e-05','0.1199650'), 
('bpa', 'cepc', '5' ) : ( '03','0.007020','4.7e-05','0.1051740'), 
('bpa', 'cepc', '10') : ( '04','0.007788','4.0e-05','0.1023830')

}

gg.update(d1)
gg.update(d2)

# (collider, decay) : ( runCode, xsec, xsecUnc )
sm = {

('cepc', 'smbb'  ) : ( '01','0.020640','0.00014'), 
('cepc', 'smmumu') : ( '01','0.006758','5.3e-05'), 
('ilc',  'smbb'  ) : ( '01','0.006698','4.3e-05'), 
('ilc',  'smmumu') : ( '01','0.001705','1.3e-05') 

}

# Check Dictionary
def checkDict():
    print "tanbeta 1"
    print "\t bma:"
    print "\t\t ", bma_bb[('1', 'cepc')]
    print "\t\t ", bma_bb[('1', 'cepc')][0]
    print "\t\t ", bma_bb[('1', 'cepc')][1]
    print "\t\t ", bma_bb[('1', 'cepc')][2]
    print "\t\t ", bma_bb[('1', 'cepc')][3]
    print "\t bpa:"
    print "\t\t ", bpa_bb[('2', 'cepc')]
    print "\t\t ", bpa_bb[('2', 'cepc')][0]
    print "\t\t ", bpa_bb[('2', 'cepc')][1]
    print "\t\t ", bpa_bb[('2', 'cepc')][2]
    print "\t\t ", bpa_bb[('2', 'cepc')][3]

    print bma_bb
    print bpa_bb

    print bma_mumu
    print bpa_mumu

    print gg

    print sm
