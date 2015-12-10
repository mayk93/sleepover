using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using VidSearch.Interfaces;

namespace VidSearch
{
    interface Presentation
    {
        private string videoPath{get; set;}
        private string entityLabel{get; set;}

        private Logic logic{get; set;}
        public List<IFrame> searchEntity() {
            if (videoPath != null && entityLabel != null)
            {
                return logic.searchEntity(videoPath, entityLabel);
            }
            else { throw new Exception("Incomplete Data!"); }
        }
    }
}
