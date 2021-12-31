"""
BSD 3-Clause License

Copyright (c) 2019, HJ Reachability Group
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Author(s): David Fridovich-Keil ( dfk@eecs.berkeley.edu )
"""
################################################################################
#
# Proximity cost for state spaces that are Cartesian products of individual
# systems' state spaces. Penalizes
#      ``` sum_{i \ne j} min(distance(i, j) - max_distance, 0)^2 ```
# for all players i, j.
#
################################################################################

import torch
import numpy as np

from cost.cost import Cost

class LaneBoundaryAdversarial(Cost):
    def __init__(self, position_indices, oriented_upward, left_boundary_x, right_boundary_x, name=""):
        """
        Initialize with dimension to add cost to and threshold BELOW which
        to impose quadratic cost.

        :param position_indices: list of index tuples corresponding to (x, y)
        :type position_indices: [(uint, uint)]
        :param max_distance: maximum value of distance to penalize
        :type max_distance: float
        """
        self._position_indices = position_indices
        self._oriented_upward = oriented_upward
        self._left_boundary_x = left_boundary_x
        self._right_boundary_x = right_boundary_x
        
        
        #self._max_distance = max_distance
        #self._num_players = len(position_indices)
        #self._player_id = int(player_id)
        super(LaneBoundaryAdversarial, self).__init__(name)

    def __call__(self, x, k=0):
        """
        Evaluate this cost function on the given state.
        NOTE: `x` should be a PyTorch tensor with `requires_grad` set `True`.
        NOTE: `x` should be a column vector.

        :param x: concatenated state vector of all systems
        :type x: torch.Tensor
        :return: scalar value of cost
        :rtype: torch.Tensor
        """
        #total_cost = torch.zeros(1, 1, requires_grad=True).double()
        # #print("Player id is: ", self._player_id)
        
        x_index, y_index = self._position_indices
        
        # if self._oriented_upward == True:
        #     if abs(self._left_boundary_x - x[x_index, 0]) <= abs(self._right_boundary_x - x[x_index, 0]):
        #         dist = x[x_index, 0] - self._left_boundary_x
    
        #     else:
        #         dist = self._right_boundary_x - x[x_index, 0]
    
        # else:
        #     if abs(self._left_boundary_x - x[x_index, 0]) <= abs(self._right_boundary_x - x[x_index, 0]):
        #         dist = self._left_boundary_x - x[x_index, 0]
    
        #     else:
        #         dist = x[x_index, 0] - self._right_boundary_x
                
        # return dist * torch.ones(1, 1, requires_grad=True).double()
        
        
        
        if self._oriented_upward == True:
            if abs(self._left_boundary_x - x[x_index, 0]) <= abs(self._right_boundary_x - x[x_index, 0]):
                dist = (x[x_index, 0] - self._left_boundary_x) * torch.ones(1, 1, requires_grad=True).double()
                return dist
    
            else:
                dist = (self._right_boundary_x - x[x_index, 0]) * torch.ones(1, 1, requires_grad=True).double()
                return dist
    
        else:
            if abs(self._left_boundary_x - x[x_index, 0]) <= abs(self._right_boundary_x - x[x_index, 0]):
                dist = (self._left_boundary_x - x[x_index, 0]) * torch.ones(1, 1, requires_grad=True).double()
                return dist
    
            else:
                dist = (x[x_index, 0] - self._right_boundary_x) * torch.ones(1, 1, requires_grad=True).double()
                return dist
                
        #return dist
        
        
        
        
        
        
        # xi_idx, yi_idx = self._position_indices[self._player_id]
        
        # for jj in range(self._num_players):
        #     if self._player_id == jj:
        #         continue
            
        #     # Compute relative distance
        #     xj_idx, yj_idx = self._position_indices[jj]
        #     dx = x[xi_idx, 0] - x[xj_idx, 0]
        #     dy = x[yi_idx, 0] - x[yj_idx, 0]
            
        #     relative_distance = torch.sqrt(dx*dx + dy*dy)
        #     #total_cost += min(relative_distance - self._max_distance, 0.0)**2
        
        # return (self._max_distance - relative_distance) * torch.ones(1, 1, requires_grad=True).double()
