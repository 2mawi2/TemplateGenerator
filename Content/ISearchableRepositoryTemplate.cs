using System.Collections.Generic;
using System.Threading.Tasks;
using Common.Model.<#package#>;
using Common.Repositories;

namespace Persistence<#package#>
{
    public interface I<#name#>Repository : ISearchableRepository<<#name#>, <#name#>.SortBy, <#name#>.FilterAttribute>
    {

    }
}