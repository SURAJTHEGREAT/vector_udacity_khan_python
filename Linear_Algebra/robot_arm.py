''' 
https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/v/projectile-height-given-time

s=V(avg)*T(change)

1 storey = 4.58 m

requirement ball has to come down in x secs


V(avg) = (Vi + Vf)/2


(total_time) = t(up) + t(down)


t(up) = (total_time)/2 = x/2

In t(up) , Vf = 0 m/s

a=-9.8m/s2 '''


''' Libraries '''


class arm_velocity_calculator(object):

    def v_average(self):
        v_avg=(self+other)/2
        return v_avg

    def time_Calc(self):
        t_up=self/2
        t_down=t_up
        return t_up,t_down

    def storey_calc(self):
        1_storey=4.58
        return self*1_storey


    def distance(self):
        velocity_avg=self.v_average
        time_up=self.time_Calc
        tot_distance=velocity_avg*time_up
        
        
