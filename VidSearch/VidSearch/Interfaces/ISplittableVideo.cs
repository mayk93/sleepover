using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace VidSearch.Interfaces
{
    interface ISplittableVideo
    {
        private List<IFrame> split();
    }
}
