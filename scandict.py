# Dictionary Format: (tanbeta, collider) : (runCode, sinbma, xsec, xsecunc) )

# sin(beta-alpha) = +1
bma = { 
    ('1' , 'cepc'):('01','1','4.306e-05','2.3e-07'),
    ('2' , 'cepc'):('02','1','4.288e-05','2.3e-07'),
    ('3' , 'cepc'):('03','1','4.265e-05','2.4e-07'),
    ('4' , 'cepc'):('04','1','4.284e-05','2.1e-07'),
    ('5' , 'cepc'):('05','1','4.313e-05','2.7e-07'),
    ('6' , 'cepc'):('06','1','4.304e-05','1.5e-07'),
    ('7' , 'cepc'):('07','1','4.324e-05','3.1e-07'),
    ('8' , 'cepc'):('08','1','4.320e-05','2.9e-07'),
    ('9' , 'cepc'):('09','1','4.319e-05','4.2e-07'),
    ('10', 'cepc'):('10','1','4.295e-05','2.5e-07'),
    ('12', 'cepc'):('11','1','4.297e-05','2.3e-07'),
    ('14', 'cepc'):('12','1','4.329e-05','2.3e-07'),
    ('16', 'cepc'):('13','1','4.288e-05','2.3e-07'),
    ('18', 'cepc'):('14','1','4.321e-05','2.7e-07'),
    ('20', 'cepc'):('15','1','4.298e-05','2.0e-07'),
    ('22', 'cepc'):('16','1','4.298e-05','3.1e-07'),
    ('24', 'cepc'):('17','1','4.311e-05','2.5e-07'),
    ('26', 'cepc'):('18','1','4.319e-05','2.3e-07'),
    ('28', 'cepc'):('19','1','4.267e-05','1.9e-07'),
    ('30', 'cepc'):('20','1','4.281e-05','2.9e-07'),
    ('32', 'cepc'):('21','1','4.298e-05','1.4e-07'),
    ('34', 'cepc'):('22','1','4.256e-05','3.3e-07'),
    ('36', 'cepc'):('23','1','4.326e-05','3.5e-07'),
    ('38', 'cepc'):('24','1','4.272e-05','2.5e-07'),
    ('40', 'cepc'):('25','1','4.322e-05','2.3e-07'),
    ('42', 'cepc'):('26','1','4.317e-05','2.9e-07'),
    ('44', 'cepc'):('27','1','4.257e-05','2.5e-07'),
    ('46', 'cepc'):('28','1','4.290e-05','1.5e-07'),
    ('48', 'cepc'):('29','1','4.299e-05','2.0e-07'),
    ('50', 'cepc'):('30','1','4.264e-05','2.3e-07'), 
    ('1' , 'ilc'):('01','1','9.562e-06','6.2e-08'),
    ('2' , 'ilc'):('02','1','9.531e-06','4.6e-08'),
    ('3' , 'ilc'):('03','1','9.545e-06','5.6e-08'),
    ('4' , 'ilc'):('04','1','9.561e-06','3.4e-08'),
    ('5' , 'ilc'):('05','1','9.619e-06','7.8e-08'),
    ('6' , 'ilc'):('06','1','9.581e-06','6.2e-08'),
    ('7' , 'ilc'):('07','1','9.633e-06','4.6e-08'),
    ('8' , 'ilc'):('08','1','9.605e-06','5.6e-08'),
    ('9' , 'ilc'):('09','1','9.600e-06','5.7e-08'),
    ('10', 'ilc'):('10','1','9.510e-06','5.0e-08'),
    ('12', 'ilc'):('11','1','9.535e-06','4.5e-08'),
    ('14', 'ilc'):('12','1','9.570e-06','5.2e-08'),
    ('16', 'ilc'):('13','1','9.498e-06','4.4e-08'),
    ('18', 'ilc'):('14','1','9.575e-06','5.1e-08'),
    ('20', 'ilc'):('15','1','9.589e-06','5.4e-08'),
    ('22', 'ilc'):('16','1','9.606e-06','3.6e-08'),
    ('24', 'ilc'):('17','1','9.557e-06','6.3e-08'),
    ('26', 'ilc'):('18','1','9.589e-06','5.1e-08'),
    ('28', 'ilc'):('19','1','9.578e-06','3.8e-08'),
    ('30', 'ilc'):('20','1','9.615e-06','3.5e-08'),
    ('32', 'ilc'):('21','1','9.525e-06','5.9e-08'),
    ('34', 'ilc'):('22','1','9.513e-06','1.0e-07'),
    ('36', 'ilc'):('23','1','9.591e-06','5.2e-08'),
    ('38', 'ilc'):('24','1','9.552e-06','7.2e-08'),
    ('40', 'ilc'):('25','1','9.618e-06','5.2e-08'),
    ('42', 'ilc'):('26','1','9.648e-06','5.3e-08'),
    ('44', 'ilc'):('27','1','9.548e-06','3.4e-08'),
    ('46', 'ilc'):('28','1','9.632e-06','4.8e-08'),
    ('48', 'ilc'):('29','1','9.567e-06','4.4e-08'),
    ('50', 'ilc'):('30','1','9.553e-06','7.0e-08') 
}

# sin(beta+alpha) = +1  ---------> sin(beta-alpha) = (tanbeta^2 - 1)/( tanbeta^2 + 1)
bpa = { 
    ('2' , 'cepc'):('31','0.6'     ,'1.812e-05','9.6e-08'),
    ('3' , 'cepc'):('32','0.8'     ,'3.070e-05','1.1e-07'),
    ('4' , 'cepc'):('33','0.882353','3.701e-05','1.5e-07'),
    ('5' , 'cepc'):('34','0.923077','4.044e-05','1.7e-07'),
    ('6' , 'cepc'):('35','0.945946','4.243e-05','2.4e-07'),
    ('7' , 'cepc'):('36','0.96'    ,'4.346e-05','1.8e-07'),
    ('8' , 'cepc'):('37','0.969231','4.411e-05','2.0e-07'),
    ('9' , 'cepc'):('38','0.97561' ,'4.506e-05','1.8e-07'),
    ('10', 'cepc'):('39','0.980198','4.526e-05','1.7e-07'),
    ('12', 'cepc'):('40','0.986207','4.586e-05','1.4e-07'),
    ('14', 'cepc'):('41','0.989848','4.608e-05','1.8e-07'),
    ('16', 'cepc'):('42','0.992218','4.614e-05','1.7e-07'),
    ('18', 'cepc'):('43','0.993846','4.637e-05','1.8e-07'),
    ('20', 'cepc'):('44','0.995012','4.654e-05','1.5e-07'),
    ('22', 'cepc'):('45','0.995876','4.667e-05','1.9e-07'),
    ('24', 'cepc'):('46','0.996534','4.653e-05','1.9e-07'),
    ('26', 'cepc'):('47','0.997046','4.641e-05','2.3e-07'),
    ('28', 'cepc'):('48','0.997452','4.679e-05','1.8e-07'),
    ('30', 'cepc'):('49','0.99778' ,'4.676e-05','1.4e-07'),
    ('32', 'cepc'):('50','0.998049','4.670e-05','1.4e-07'),
    ('34', 'cepc'):('51','0.998271','4.692e-05','1.7e-07'),
    ('36', 'cepc'):('52','0.998458','4.676e-05','1.8e-07'),
    ('38', 'cepc'):('53','0.998616','4.675e-05','2.3e-07'),
    ('40', 'cepc'):('54','0.998751','4.689e-05','1.7e-07'),
    ('42', 'cepc'):('55','0.998867','4.721e-05','1.9e-07'),
    ('44', 'cepc'):('56','0.998967','4.716e-05','1.8e-07'),
    ('46', 'cepc'):('57','0.999055','4.684e-05','1.4e-07'),
    ('48', 'cepc'):('58','0.999132','4.710e-05','1.8e-07'),
    ('50', 'cepc'):('59','0.9992'  ,'4.708e-05','1.9e-07'),
    ('2' , 'ilc'):('31','0.6'     ,'4.369e-06','1.8e-08'),
    ('3' , 'ilc'):('32','0.8'     ,'7.272e-06','2.9e-08'),
    ('4' , 'ilc'):('33','0.882353','8.673e-06','3.8e-08'),
    ('5' , 'ilc'):('34','0.923077','9.418e-06','3.2e-08'),
    ('6' , 'ilc'):('35','0.945946','9.941e-06','4.9e-08'),
    ('7' , 'ilc'):('36','0.96'    ,'1.018e-05','4.1e-08'),
    ('8' , 'ilc'):('37','0.969231','1.033e-05','6.1e-08'),
    ('9' , 'ilc'):('38','0.97561' ,'1.051e-05','4.1e-08'),
    ('10', 'ilc'):('39','0.980198','1.058e-05','4.6e-08'),
    ('12', 'ilc'):('40','0.986207','1.062e-05','4.4e-08'),
    ('14', 'ilc'):('41','0.989848','1.080e-05','4.3e-08'),
    ('16', 'ilc'):('42','0.992218','1.084e-05','4.4e-08'),
    ('18', 'ilc'):('43','0.993846','1.086e-05','3.5e-08'),
    ('20', 'ilc'):('44','0.995012','1.088e-05','4.4e-08'),
    ('22', 'ilc'):('45','0.995876','1.087e-05','5.0e-08'),
    ('24', 'ilc'):('46','0.996534','1.082e-05','4.3e-08'),
    ('26', 'ilc'):('47','0.997046','1.088e-05','4.5e-08'),
    ('28', 'ilc'):('48','0.997452','1.098e-05','3.5e-08'),
    ('30', 'ilc'):('49','0.99778' ,'1.096e-05','6.2e-08'),
    ('32', 'ilc'):('50','0.998049','1.096e-05','6.1e-08'),
    ('34', 'ilc'):('51','0.998271','1.096e-05','3.5e-08'),
    ('36', 'ilc'):('52','0.998458','1.095e-05','4.9e-08'),
    ('38', 'ilc'):('53','0.998616','1.091e-05','4.3e-08'),
    ('40', 'ilc'):('54','0.998751','1.090e-05','4.6e-08'),
    ('42', 'ilc'):('55','0.998867','1.099e-05','4.5e-08'),
    ('44', 'ilc'):('56','0.998967','1.104e-05','5.3e-08'),
    ('46', 'ilc'):('57','0.999055','1.091e-05','5.0e-08'),
    ('48', 'ilc'):('58','0.999132','1.100e-05','4.4e-08'),
    ('50', 'ilc'):('59','0.9992'  ,'1.102e-05','7.7e-08')
}

d1 = { ('bma','ilc',  '{i}'.format(i=i)): ( '01','0.0018030','1.2e-05','0.0815942') for i in range(1,51) }
d2 = { ('bma','cepc', '{i}'.format(i=i)): ( '01','0.008177','5.8e-05','0.0815942')  for i in range(1,51) }

# (scenario, collider, tanbeta) : ( runCode, xsec, xsecUnc, branchingRatio)
gg ={ 
    
('bpa', 'ilc,','2' ) : ( '02','0.0006564','3.4e-06','0.1199650'),
('bpa', 'ilc,','5' ) : ( '03','0.0015390','1.0e-05','0.1051740'),
('bpa', 'ilc,','10') : ( '04','0.0017200','9.3e-06','0.1023830'),

('bpa', 'cepc', '2' ) : ( '02','0.002966','2.0e-05','0.1199650'), 
('bpa', 'cepc', '5' ) : ( '03','0.007020','4.7e-05','0.1051740'), 
('bpa', 'cepc', '10') : ( '04','0.007788','4.0e-05','0.1023830')

}

gg.update(d1)
gg.update(d2)


# Check Dictionary
def checkDict():
    print "tanbeta 1"
    print "\t bma:"
    print "\t\t ", bma[('1', 'cepc')]
    print "\t\t ", bma[('1', 'cepc')][0]
    print "\t\t ", bma[('1', 'cepc')][1]
    print "\t\t ", bma[('1', 'cepc')][2]
    print "\t\t ", bma[('1', 'cepc')][3]
    print "\t bpa:"
    print "\t\t ", bpa[('2', 'cepc')]
    print "\t\t ", bpa[('2', 'cepc')][0]
    print "\t\t ", bpa[('2', 'cepc')][1]
    print "\t\t ", bpa[('2', 'cepc')][2]
    print "\t\t ", bpa[('2', 'cepc')][3]


    print gg
