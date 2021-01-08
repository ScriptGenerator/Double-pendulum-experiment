from uncertainties import ufloat
import pandas as pd
import plotly.express as px
import csv

# importing the file that contains all the measured data
#df = pd.read_csv('C:\\Users\\ahmed\\OneDrive\\Desktop\\fulldata.csv')
df = pd.read_csv('C:\\Users\\ahmed\\OneDrive\\Desktop\\full experiment data.tsv', sep='\t', quoting=csv.QUOTE_NONE) 


# calculating dt
frame_rate = 60
time_required_to_record_one_frame = 1/frame_rate

# converting the mass to kg after we measured the mass in grams using a scale with an accuracy of 3 decimal points
mass = ufloat(10, 0.0005)/1000
# converting to use meters insead of centimeters
total_length = ufloat(38, 0.05)/100


# defining and importing the measured variables
time = df['Time (t) (seconds)']
x_position_of_point_mass1 = df['x coordinate for point mass 1']
y_position_of_point_mass1 = df['y coordinate for point mass 1']
x_position_of_point_mass2 = df['x coordinate for point mass 2']
y_position_of_point_mass2 = df['y coordinate for point mass 2']

#defining the variables that will be obtained
x_velocity_of_point_mass1 = []
y_velocity_of_point_mass1 = []
total_velocity_of_point_mass1 = []
kinetic_energy_of_point_mass1 = []
potential_energy_of_point_mass1 = []
total_energy_of_point_mass1 = []

x_velocity_of_point_mass2 = []
y_velocity_of_point_mass2 = []
total_velocity_of_point_mass2 = []
kinetic_energy_of_point_mass2 = []
potential_energy_of_point_mass2 = []
total_energy_of_point_mass2 = []


#defining the uncertainties for each variable
x_velocity_of_point_mass1_uncertainty = []
y_velocity_of_point_mass1_uncertainty = []
total_velocity_of_point_mass1_uncertainty = []
kinetic_energy_of_point_mass1_uncertainty = []
potential_energy_of_point_mass1_uncertainty = []
total_energy_of_point_mass1_uncertainty = []

x_velocity_of_point_mass2_uncertainty = []
y_velocity_of_point_mass2_uncertainty = []
total_velocity_of_point_mass2_uncertainty = []
kinetic_energy_of_point_mass2_uncertainty = []
potential_energy_of_point_mass2_uncertainty = []
total_energy_of_point_mass2_uncertainty = []

# idk yet
total_energy_of_system = []


total_energy_of_system_uncertainty = []

def get_velocity(initial_position, final_position):
	#change in position between frame n-1 and n+1
	change_in_position = ufloat(final_position, 0.0025) - ufloat(initial_position, 0.0025)
	# double the amount of time that it takes to record one frame.
	change_in_time = 2*ufloat(time_required_to_record_one_frame, 0.0083)
	velocity = change_in_position/change_in_time
	#return velocity.n, velocity.s
	return velocity


for index in range(len(time)):
	if index > 0 and index < 1001 :
		x_velocity_of_point_mass1.append(get_velocity(x_position_of_point_mass1[index-1], x_position_of_point_mass1[index+1]))
		y_velocity_of_point_mass1.append(get_velocity(y_position_of_point_mass1[index-1], y_position_of_point_mass1[index+1]))

		x_velocity_of_point_mass2.append(get_velocity(x_position_of_point_mass2[index-1], x_position_of_point_mass2[index+1]))
		y_velocity_of_point_mass2.append(get_velocity(y_position_of_point_mass2[index-1], y_position_of_point_mass2[index+1]))


for index in range(len(time)):
	if index > 0 and index < 999 :
		total_velocity_of_point_mass1.append((x_velocity_of_point_mass1[index+1]**(2) + y_velocity_of_point_mass1[index+1]**(2))**(1/2))
		total_velocity_of_point_mass2.append((x_velocity_of_point_mass2[index+1]**(2) + y_velocity_of_point_mass2[index+1]**(2))**(1/2))

for index in range(len(time)):
	if index > 0 and index < 999 :
		# calculating the instantanious kinetic energy and instantanious potential energy for each point mass
		kinetic1 = (mass/2)*(total_velocity_of_point_mass1[index-1]**2)
		kinetic2 = (mass/2)*(total_velocity_of_point_mass2[index-1]**2)
		potential1 = mass*9.81*(y_position_of_point_mass1[index+2]+total_length)
		potential2 = mass*9.81*(y_position_of_point_mass2[index+2]+total_length)

		# calculating the sum of insantaneous energies for each point mass
		total_energy1 = kinetic1 + potential1
		total_energy2 = kinetic2 + potential2

		# calculating the instantaneous total energy of the system by summing the total energies of all point masses
		instantaneous_total_energy_of_the_system = total_energy1 + total_energy2

		# seperating all the estimated results into different lists so the data can be plotted later on
		kinetic_energy_of_point_mass1.append(kinetic1.n)
		kinetic_energy_of_point_mass2.append(kinetic2.n)

		potential_energy_of_point_mass1.append(potential1.n)
		potential_energy_of_point_mass2.append(potential2.n)

		total_energy_of_point_mass1.append(total_energy1.n)
		total_energy_of_point_mass2.append(total_energy2.n)

		total_energy_of_system.append(instantaneous_total_energy_of_the_system.n)

		# obtaining all the uncertainties of the estimated results into different lists for later use
		kinetic_energy_of_point_mass1_uncertainty.append(kinetic1.s)
		kinetic_energy_of_point_mass2_uncertainty.append(kinetic2.s)

		potential_energy_of_point_mass1_uncertainty.append(potential1.s)
		potential_energy_of_point_mass2_uncertainty.append(potential2.s)

		total_energy_of_point_mass1_uncertainty.append(total_energy1.s)
		total_energy_of_point_mass2_uncertainty.append(total_energy2.s)

		total_energy_of_system_uncertainty.append(instantaneous_total_energy_of_the_system.s)











