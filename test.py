from unittest import TestCase
import unittest
from pyunitreport import HTMLTestRunner
from socialChoice import SocialChoice

##### Test Class #####

class test(TestCase):

	def setUp(self):

		self.socialChoice = SocialChoice()

		self.preferences = {
			'u1':{
				'c1': 2,
				'c2': 6,
				'c3': 8
			},
			'u2':{
				'c1': 4,
				'c2': 5,
				'c3': 3
			},
			'u3':{
				'c1': 9,
				'c2': 0,
				'c3': 9
			}
		}


		self.configuration_users_satisfaction_winner = 'c3'

		self.configuration_users_satisfaction_result = {
			'u1': 8,
			'u2': 3,
			'u3': 9
		}




	## Templates ##

	def template_test_method_dict(self, method, arg, expected):
		print(str('Testing {}').format(method.__name__))
		print('arg', arg)
		if isinstance(arg, list):
			if len(arg) == 2:
				response = method(arg[0], arg[1])
			elif len(arg) == 3:
				response = method(arg[0], arg[1], arg[2])
			else:
				pass
		else:
			response = method(arg)

		print("Arg: ", arg)
		print("Excepted: ", expected)
		print("Response: ", response)

		self.assertDictEqual(response, expected)

	def template_test_method_list(self, method, arg, expected):
		print(str('Testing {}').format(method.__name__))

		if isinstance(arg, list):
			if len(arg) == 2:
				response = method(arg[0], arg[1])
			if len(arg) == 3:
				response = method(arg[0], arg[1], arg[2])
		else:
			response = method(arg)

		print("Arg: ", arg)
		print("Excepted: ", expected)
		print("Response: ", response)

		self.assertListEqual(response, expected)

	def template_test_method_int(self, method, arg, expected):
		print(str('Testing {}').format(method.__name__))

		if isinstance(arg, list):
			if len(arg) == 2:
				response = method(arg[0], arg[1])
			if len(arg) == 3:
				response = method(arg[0], arg[1], arg[2])
		else:
			response = method(arg)

		print("Arg: ", arg)
		print("Excepted: ", expected)
		print("Response: ", response)

		self.assertEqual(response, expected)



	## Tests##

	def test01_sum_preferences_votes(self):

		sum_preferences_votes = {
			'c1': 15,
			'c2': 11,
			'c3': 20
		}

		self.template_test_method_dict(self.socialChoice.sum_preferences_votes, self.preferences, sum_preferences_votes)


	def test02_sort_configurations(self):

		sort_configurations = ['c3', 'c1', 'c2']
		preferences_votes = {'c1': 15, 'c2': 11, 'c3': 20}

		self.template_test_method_list(self.socialChoice.sort_configurations, preferences_votes, sort_configurations)


	def test03_sum_configuration_votes(self):

		sum_configuration_votes = 16

		self.template_test_method_int(self.socialChoice.sum_configuration_votes, self.preferences['u1'], sum_configuration_votes)


	def test04_count_number_keys(self):
		
		count_number_keys = 3

		self.template_test_method_int(self.socialChoice.count_number_keys, self.preferences['u1'], count_number_keys)

	def test05_filter_preferences_maximum_voting_value(self):

		maximum_voting_value_preferences = {
			'u1':{
				'c1': 12,
				'c2': 10,
				'c3': 7
			},
			'u2':{
				'c1': 5,
				'c2': 7,
				'c3': 15
			},
			'u3':{
				'c1': 10,
				'c2': 22,
				'c3': 30
			}
		}

		maximum_voting_value = {
			'u1':{
				'c1': 10,
				'c2': 10,
				'c3': 7
			},
			'u2':{
				'c1': 5,
				'c2': 7,
				'c3': 10
			},
			'u3':{
				'c1': 10,
				'c2': 10,
				'c3': 10
			}
		}

		self.template_test_method_dict(self.socialChoice.filter_preferences_maximum_voting_value, maximum_voting_value_preferences, maximum_voting_value)

	def test05_filter_preferences_maximum_total_votes(self):

		maximum_total_votes_preferences = {
			'u1':{
				'c1': 8,
				'c2': 10,
				'c3': 5
			},
			'u2':{
				'c1': 5,
				'c2': 7,
				'c3': 15
			},
			'u3':{
				'c1': 10,
				'c2': 22,
				'c3': 30
			}
		}

		maximum_total_votes = {
			'u1':{
				'c1': 8,
				'c2': 10,
				'c3': 2
			},
			'u2':{
				'c1': 5,
				'c2': 7,
				'c3': 8
			},
			'u3':{
				'c1': 10,
				'c2': 10,
				'c3': 0
			}
		}

		self.template_test_method_dict(self.socialChoice.filter_preferences_maximum_total_votes, maximum_total_votes_preferences, maximum_total_votes)


		## Greater Preferences
	def test05_greater_preferences(self):

		greater_preferences = {
			'u1':{
				'c1': 0,
				'c2': 0,
				'c3': 1
			},
			'u2':{
				'c1': 0,
				'c2': 1,
				'c3': 0
			},
			'u3':{
				'c1': 1,
				'c2': 0,
				'c3': 0
			}
		}

		self.template_test_method_dict(self.socialChoice.greater_preferences, self.preferences, greater_preferences)


	def test06_greater_preferences_multiple(self):
		
		greater_preferences_multiple = {
			'u1':{
				'c1': 0,
				'c2': 0,
				'c3': 1
			},
			'u2':{
				'c1': 0,
				'c2': 1,
				'c3': 0
			},
			'u3':{
				'c1': 1/2,
				'c2': 0,
				'c3': 1/2
			}
		}

		self.template_test_method_dict(self.socialChoice.greater_preferences_multiple, self.preferences, greater_preferences_multiple)

	def test07_binary_preferences(self):

		binary_preferences = {
			'u1':{
				'c1': 1,
				'c2': 1,
				'c3': 1
			},
			'u2':{
				'c1': 1,
				'c2': 1,
				'c3': 1
			},
			'u3':{
				'c1': 1,
				'c2': 0,
				'c3': 1
			}
		}

		self.template_test_method_dict(self.socialChoice.binary_preferences, self.preferences, binary_preferences)

	def test08_descending_preferences(self):
		
		descending_preferences = {
			'u1':{
				'c1': 0,
				'c2': 1,
				'c3': 2
			},
			'u2':{
				'c1': 1,
				'c2': 2,
				'c3': 0
			},
			'u3':{
				'c1': 2,
				'c2': 0,
				'c3': 1
			}
		}

		self.template_test_method_dict(self.socialChoice.descending_preferences, self.preferences, descending_preferences)



	def test09_normalized_preferences(self):

		normalized_preferences = {
			'u1':{
				'c1': 2/(2+6+8),
				'c2': 6/(2+6+8),
				'c3': 8/(2+6+8)
			},
			'u2':{
				'c1': 4/(4+5+3),
				'c2': 5/(4+5+3),
				'c3': 3/(4+5+3)
			},
			'u3':{
				'c1': 9/(9+0+9),
				'c2': 0/(9+0+9),
				'c3': 9/(9+0+9)
			}
		}

		self.template_test_method_dict(self.socialChoice.normalized_preferences, self.preferences, normalized_preferences)


	def test10_plurality_voting(self):

		preferences_plurality_voting = {
			'u1':{
				'c1': 8,
				'c2': 4,
				'c3': 7
			},
			'u2':{
				'c1': 1,
				'c2': 4,
				'c3': 9
			},
			'u3':{
				'c1': 9,
				'c2': 4,
				'c3': 4
			}
		}

		plurality_voting = ['c1', 'c3', 'c2']

		self.template_test_method_list(self.socialChoice.plurality_voting, preferences_plurality_voting, plurality_voting)


	def test11_borda_voting(self):

		preferences_borda_voting = {
			'u1':{
				'c1': 9, #2
				'c2': 5, #1
				'c3': 2  #0
			},
			'u2':{
				'c1': 9, #2
				'c2': 5, #1
				'c3': 2  #0
			},
			'u3':{
				'c1': 5, #1
				'c2': 9, #2
				'c3': 2  #0
			}
		}

		borda_voting = ['c1', 'c2', 'c3']

		self.template_test_method_list(self.socialChoice.borda_voting, preferences_borda_voting, borda_voting)


	def test12_range_voting(self):

		preferences_range_voting = {
			'u1':{
				'c1': 4, 
				'c2': 3, 
				'c3': 7  
			},
			'u2':{
				'c1': 3, 
				'c2': 4, 
				'c3': 5  
			},
			'u3':{
				'c1': 9, 
				'c2': 2, 
				'c3': 1  
			}
		}

		range_voting = ['c1', 'c3', 'c2']

		self.template_test_method_list(self.socialChoice.range_voting, preferences_range_voting, range_voting)


	def test13_approval_voting(self):

		preferences_approval_voting = {
			'u1':{
				'c1': 4, 
				'c2': 0, 
				'c3': 7  
			},
			'u2':{
				'c1': 9, 
				'c2': 0, 
				'c3': 1  
			},
			'u3':{
				'c1': 0, 
				'c2': 4, 
				'c3': 1  
			}
		}

		approval_voting = ['c3', 'c1', 'c2']

		self.template_test_method_list(self.socialChoice.approval_voting, preferences_approval_voting, approval_voting)


	def test14_cumulative_voting(self):

		preferences_cumulative_voting = {
			'u1':{
				'c1': 14, 
				'c2': 5, 
				'c3': 1  
			},
			'u2':{
				'c1': 5, 
				'c2': 5, 
				'c3': 10  
			},
			'u3':{
				'c1': 10, 
				'c2': 6, 
				'c3': 9  
			}
		}

		cumulative_voting = ['c1', 'c2', 'c3']

		self.template_test_method_list(self.socialChoice.cumulative_voting, preferences_cumulative_voting, cumulative_voting)

	def test15_service_users_satisfaction(self):

		preferences_service_users_satisfaction = {
			'u1':{
				'c1': 7, 
				'c2': 3, 
				'c3': 5  
			},
			'u2':{
				'c1': 8, 
				'c2': 5, 
				'c3': 3  
			},
			'u3':{
				'c1': 2, 
				'c2': 8, 
				'c3': 2  
			}
		}

		winner = 'c1'

		service_users_satisfaction = {
			'u1': 7,
			'u2': 8,
			'u3': 2
		}


		self.template_test_method_dict(self.socialChoice.service_users_satisfaction, [preferences_service_users_satisfaction, winner], service_users_satisfaction)


	def test16_total_service_satisfaction(self):

		configuration_users_satisfaction = {
			'u1': 7,
			'u2': 8,
			'u3': 2
		}

		total_service_satisfaction = 17

		self.template_test_method_int(self.socialChoice.total_service_satisfaction, configuration_users_satisfaction, total_service_satisfaction)


	def test17_average_service_satisfaction(self):

		configuration_users_satisfaction = {
			'u1': 7,
			'u2': 8,
			'u3': 2
		}

		average_service_satisfaction = (8+7+2)/3

		self.template_test_method_int(self.socialChoice.average_service_satisfaction, configuration_users_satisfaction, average_service_satisfaction)


	def test18_normalized_service_satisfaction(self):

		configuration_users_satisfaction = {
			'u1': 7,
			'u2': 8,
			'u3': 2
		}

		normalized_service_satisfaction = ((8+7+2)/3)/10

		self.template_test_method_int(self.socialChoice.normalized_service_satisfaction, configuration_users_satisfaction, normalized_service_satisfaction)



	def test19_services_winning_configurations(self):

		services = {
	        's1':{
	            'u1':{
	                'c1': 8,
	                'c2': 5,
	                'c3': 3
	            },
	            'u2':{
	                'c1': 3,
	                'c2': 9,
	                'c3': 5
	            },
	            'u3':{
	                'c1': 3,
	                'c2': 9,
	                'c3': 5
	            }
	        },
	        's2':{
	            'u1':{
	                'c1': 3,
	                'c2': 7,
	                'c3': 4
	            },
	            'u2':{
	                'c1': 3,
	                'c2': 7,
	                'c3': 2
	            },
	            'u3':{
	                'c1': 3,
	                'c2': 9,
	                'c3': 5
	            }
	   		}
	    }

		services_winning_configurations_plurality_voting = {'s1':self.socialChoice.plurality_voting(services.get('s1')),
															's2':self.socialChoice.plurality_voting(services.get('s2'))}
		services_winning_configurations_borda_voting = {'s1':self.socialChoice.borda_voting(services.get('s1')),
														's2':self.socialChoice.borda_voting(services.get('s2'))}
		services_winning_configurations_range_voting = {'s1':self.socialChoice.range_voting(services.get('s1')),
														's2':self.socialChoice.range_voting(services.get('s2'))}
		services_winning_configurations_approval_voting = {'s1':self.socialChoice.approval_voting(services.get('s1')),
														   's2':self.socialChoice.approval_voting(services.get('s2'))}
		services_winning_configurations_cumulative_voting = {'s1':self.socialChoice.cumulative_voting(services.get('s1')),
							    							 's2':self.socialChoice.cumulative_voting((services.get('s2')))}
		

		self.template_test_method_dict(self.socialChoice.services_winning_configurations, [services, 'plurality_voting'], services_winning_configurations_plurality_voting)
		self.template_test_method_dict(self.socialChoice.services_winning_configurations, [services, 'borda_voting'], services_winning_configurations_borda_voting)
		self.template_test_method_dict(self.socialChoice.services_winning_configurations, [services, 'range_voting'], services_winning_configurations_range_voting)
		self.template_test_method_dict(self.socialChoice.services_winning_configurations, [services, 'approval_voting'], services_winning_configurations_approval_voting)
		self.template_test_method_dict(self.socialChoice.services_winning_configurations, [services, 'cumulative_voting'], services_winning_configurations_cumulative_voting)


	def test20_total_global_services_satisfaction(self):

		configuration_users_satisfaction = {
			'u1': 7,
			'u2': 8,
			'u3': 2
		}

		total_global_services_satisfaction = ((8+7+2)/3)/10

		self.template_test_method_int(self.socialChoice.total_global_services_satisfaction, configuration_users_satisfaction, normalized_service_satisfaction)

if __name__ == '__main__':
	unittest.TestLoader.sortTestMethodsUsing = None
	unittest.main(testRunner=HTMLTestRunner(output='APIRest_test'), failfast=True)
